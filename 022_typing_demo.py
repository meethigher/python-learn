# typing_demo.py - typing 注解示例
from typing import List, Dict, Tuple

def summarize(values: List[int]) -> Dict[str, float]:
    return {'count': len(values), 'avg': sum(values)/len(values) if values else 0.0}

def main():
    print(summarize([1,2,3,4]))

if __name__ == '__main__':
    main()
