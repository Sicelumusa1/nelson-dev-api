from flask import Blueprint, request, Response
import json
from typing import Dict, Any

re_arranger = Blueprint(
    're_arranger', 
    __name__, 
    template_folder='template'
)

@re_arranger.route('/', methods=['POST'])
def rearranger() -> Dict[str, Any]:
    
    # Validate request content type first
    if not request.is_json:
        return Response(
                json.dumps({"error": "Request must be JSON"}, separators=(",", ":")),
                status=400,
                mimetype="application/json"
            )
    try:
        data = request.get_json()
        
        # Validate data structure
        if not data or 'data' not in data:
            return Response(
                json.dumps({"error": "Missing 'data' in request body"}, separators=(",", ":")),
                status=400,
                mimetype="application/json"
            )
        
        input_str = data['data']

        # Validate input type
        if not isinstance(input_str, str):
            return Response(
                json.dumps({"error": "'data' must be a string"}, separators=(",", ":")),
                status=400,
                mimetype="application/json"
            )
            
        # Validate input content
        if not input_str.strip():
            return Response(
                json.dumps({"error": "'data' cannot be empty"}, separators=(",", ":")),
                status=400,
                mimetype="application/json"
            )
            
        # Process the string
        sorted_array = sorted(input_str)

        return Response(
                json.dumps({"word": sorted_array}, indent=None),
                status=200,
                mimetype="application/json"
            )
    except json.JSONDecodeError:
        return Response(
                json.dumps({"error": "Invalid JSON format"}, separators=(",", ":")),
                status=400,
                mimetype="application/json"
            )
    
    except Exception as e:
        return Response(
                json.dumps({"error": f"Internal Server Error: {str(e)}"}, separators=(",", ":")),
                status=500,
                mimetype="application/json"
            )

    