import time
import sys

def run_lirik():
    lirik = [
        "Timbul di dalam dada...",
        "Pada pandangan pertama...",
        "Dari situlah aku terlena..."
    ]

    delay = [0.10, 0.10, 0.10]
    print("=== Tisa Monica ===")
    time.sleep(1)

    for i, baris_lagu in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay[i])
        print()
        time.sleep(delay[i])

run_lirik()

def run_lirik():
    lirik = [
        "Oh adek tia monica...",
        "Apakah mau...",
        "Jadi pacar kandaaa..."
    ]

    delay = [0.10, 0.10, 0.10]
    time.sleep(1)

    for i, baris_lagu in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay[i])
        print()
        time.sleep(delay[i])

run_lirik()