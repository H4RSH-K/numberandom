from datetime import datetime
import math

def numberandom():
    random=datetime.now().strftime("%S")
    numberand=pow(int(random), int(random))
    return numberand

if __name__ == "__main__":
    print("RANDOM NUMBER : %d", numberandom())
