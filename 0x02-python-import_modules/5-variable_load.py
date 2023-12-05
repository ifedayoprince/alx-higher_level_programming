#!/usr/bin/python3
import variable_load_5
if __name__ == "__main__":  
    filtered = filter(lambda name: not name.startswith("__"), dir(variable_load_5))
    print(filtered)
