# bloom_loader.py
import pybloomfilter

BLOOM = pybloomfilter.BloomFilter.open("api/compromised.bloom")
