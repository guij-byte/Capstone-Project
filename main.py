from risk_analyzer import RiskAnalyzer
from predictor import Predictor
from ci_integration_agent import CIIntegrationAgent
from auto_repair_generator import AutoRepairGenerator
from log_config import setup_logging

setup_logging()

source_context = "def example(): print('Hello')"
features = {"func_calls": 4, "lib_used": 1, "lines_of_code": 25}

analyzer = RiskAnalyzer()
predictor = Predictor()
ci = CIIntegrationAgent()
repair = AutoRepairGenerator()

analyzer.incorporate_git_history(source_context)
result = predictor.predict_vulnerabilities(features)

ci.handle_push_event()
repair.handle_push_event()
