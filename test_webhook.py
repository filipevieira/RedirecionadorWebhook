import os
import logging
import unittest
from unittest.mock import patch

from WebhookRediGlobal import app, run_server


class ServerConfigurationTests(unittest.TestCase):
    @patch("WebhookRediGlobal.app.run")
    def test_production_disables_debug_and_uses_localhost(self, mock_run):
        with patch.dict(
            os.environ,
            {"APP_ENV": "production", "FLASK_DEBUG": "true", "PORT": "5000"},
            clear=True,
        ):
            run_server()

        mock_run.assert_called_once_with(
            host="127.0.0.1",
            port=5000,
            debug=False,
            use_reloader=False,
        )

    @patch("WebhookRediGlobal.app.run")
    def test_debug_requires_explicit_development_configuration(self, mock_run):
        with patch.dict(
            os.environ,
            {
                "APP_ENV": "development",
                "FLASK_DEBUG": "true",
                "FLASK_HOST": "127.0.0.1",
                "PORT": "5000",
            },
            clear=True,
        ):
            run_server()

        mock_run.assert_called_once_with(
            host="127.0.0.1",
            port=5000,
            debug=True,
            use_reloader=False,
        )


class WebhookBehaviorTests(unittest.TestCase):
    @patch("WebhookRediGlobal.threading.Thread")
    def test_webhook_response_and_forwarding_are_preserved(self, mock_thread):
        if not app.logger.handlers:
            app.logger.addHandler(logging.NullHandler())

        response = app.test_client().post(
            "/api/webhooks/incoming/omie/example",
            json={"topic": "invoice.created"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(),
            {
                "reenviado_para": (
                    "https://devi-sandbox.azurewebsites.net/"
                    "api/webhooks/incoming/omie/example"
                ),
                "topico": "invoice.created",
            },
        )
        mock_thread.assert_called_once()
        mock_thread.return_value.start.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
