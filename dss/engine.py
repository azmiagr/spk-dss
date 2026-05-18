import math
from typing import List, Dict, Any, Literal

class Criterion:
    def __init__(self, criteria_code: str, attribute_type: Literal['benefit', 'cost'], weight: float):
        self.code = criteria_code
        self.type = attribute_type
        self.weight = weight

class SAWMethod:
    
    def calculate(self, criteria: List[Criterion], alternatives: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        if not alternatives or not criteria:
            return []

        total_weight = sum(c.weight for c in criteria)
        normalized_weights = {c.code: (c.weight / total_weight) for c in criteria}

        min_max_values = {}
        for c in criteria:
            values = [alt.get(c.code, 0) for alt in alternatives]
            min_max_values[c.code] = {
                "max": max(values) if values else 0,
                "min": min(values) if values else 0
            }

        results = []
        
        for alt in alternatives:
            score = 0.0
            normalized_data = {}
            
            for c in criteria:
                val = alt.get(c.code, 0)
                c_max = min_max_values[c.code]["max"]
                c_min = min_max_values[c.code]["min"]
                
                norm_val = 0.0
                if c.type == 'benefit' and c_max != 0:
                    norm_val = val / c_max
                elif c.type == 'cost' and val != 0:
                    norm_val = c_min / val
                
                normalized_data[c.code] = norm_val
                
                score += norm_val * normalized_weights[c.code]
            
            result_item = alt.copy()
            result_item["normalized"] = normalized_data
            result_item["score"] = score
            results.append(result_item)
            
        results.sort(key=lambda x: x["score"], reverse=True)
        return results