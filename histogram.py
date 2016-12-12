import sys

def histogram(text):
    
    histogram = {}
    split_text = text.split(" ")
    
    for wyraz in split_text:
        if len(wyraz) in histogram:
            histogram[len(wyraz)] += 1
        else:
            histogram[len(wyraz)] = 1
    
    return histogram
