import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'automation'))
from analyze_proposal import analyze

def test_neighbor_results_are_advisory():
 result=analyze('Techmate','An AI collaborator used as a recurring teammate for technical work.')
 assert result
 assert 'advisory_relation' in result[0]
