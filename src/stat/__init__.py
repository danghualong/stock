from flask import Blueprint

stat_bp = Blueprint("stat", __name__, url_prefix="/stat")

from .controller import break_point
from .controller import stock_filter 