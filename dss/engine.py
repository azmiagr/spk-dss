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

        # 1. Normalisasi Bobot (Pastikan total bobot = 1)
        total_weight = sum(c.weight for c in criteria)
        normalized_weights = {c.code: (c.weight / total_weight) for c in criteria}

        # 2. Cari nilai Max dan Min untuk setiap kriteria
        min_max_values = {}
        for c in criteria:
            # Mengambil semua nilai untuk kriteria ini dari setiap alternatif
            values = [alt.get(c.code, 0) for alt in alternatives]
            min_max_values[c.code] = {
                "max": max(values) if values else 0,
                "min": min(values) if values else 0
            }

        results = []
        
        # 3. Proses Normalisasi Matriks & 4. Perhitungan Nilai Preferensi
        for alt in alternatives:
            score = 0.0
            normalized_data = {}
            criteria_scores = {}
            
            for c in criteria:
                val = alt.get(c.code, 0)
                c_max = min_max_values[c.code]["max"]
                c_min = min_max_values[c.code]["min"]
                
                # Menghindari pembagian dengan 0
                norm_val = 0.0
                if c.type == 'benefit' and c_max != 0:
                    norm_val = val / c_max
                elif c.type == 'cost' and val != 0:
                    norm_val = c_min / val
                
                normalized_data[c.code] = norm_val
                
                # Mengalikan dengan bobot yang sudah dinormalisasi
                weighted_score = norm_val * normalized_weights[c.code]
                criteria_scores[c.code] = weighted_score
                score += weighted_score
            
            # Menyimpan hasil
            result_item = alt.copy()
            result_item["normalized"] = normalized_data
            result_item["criteria_scores"] = criteria_scores
            result_item["score"] = score
            result_item["price"] = alt.get("price", alt.get("C4", 0))
            results.append(result_item)
            
        # 5. Perankingan (Sort descending berdasarkan skor)
        results.sort(key=lambda x: x["score"], reverse=True)
        return results