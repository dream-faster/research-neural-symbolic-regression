from random import choice, uniform
from typing import List, Tuple
from utils.lis import eval_lisp, parse
import numpy as np

LispProgram = str

Operator = str
Constant = str

def add_next_op(program: LispProgram, op: Operator, constant: Constant, list_of_binary_ops: List[Operator], list_of_unary_ops: List[Operator]) -> LispProgram:
    if op in list_of_binary_ops:
        return "( " + op + " " + constant + " " + program + " )"
    elif op in list_of_unary_ops:
        return "( " + op + " " + program + " )"
    else:
        raise(Exception("Invalid operator"))


def generate_random_eq(binary_operators: List[Operator], unary_operators: List[Operator], length: int) -> LispProgram:

    def generate_next(ops: List[str]) -> Tuple[Operator, Constant, List[str]]:
        random_float = round(uniform(0.0, 1000.0), 2)	
        ops = ops.copy()
        op = choice(ops)
        ops.remove(op)
        return (op, str(np.random.choice([random_float, "t"], p = [0.9, 0.1])), ops)

    program = str("t")
    operators = binary_operators + unary_operators
    for _ in range(0, length):
        op, constant, operators = generate_next(operators)
        program = add_next_op(program, op, constant, binary_operators, unary_operators)
    return program

def generate_random_eq_valid(operators: List[str], length: int) -> str:
    valid = False
    while valid == False:
        eq = generate_random_eq(operators, length)
        valid = is_eq_valid(eq)
    return eq


def is_eq_valid(eq: LispProgram, test_set: List[int] = [1,2,4,5,10]) -> bool:
    try:
        results = [eval_lisp(parse(eq.replace('t', str(num)))) for num in test_set]
        if len(set(results)) == 1:
            return False
        else:
            return True
    except:
        return False


def eq_to_seq(eq: LispProgram, length: int) -> List[int]:
    int_seq: List[int] = []
    for i in range(0, length):
        try:
            int_seq.append(int(eval_lisp(parse(eq.replace('t', str(i+1))))))
        except:
            pass
    if len(int_seq) != length: return [0] * length
    return int_seq
