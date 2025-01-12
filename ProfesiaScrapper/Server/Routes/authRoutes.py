from flask import Blueprint, jsonify, request, abort
import firebase_admin
from firebase_admin import auth

authRoutesBlueprint = Blueprint('auth', __name__)