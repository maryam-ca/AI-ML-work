# Day 13 - Ingestion Pipeline

## Overview
This module loads documents, splits them into chunks, creates embeddings, and stores them in Qdrant.

## Structure
- src/app → logic
- scripts → runnable files
- data → input documents

## Run
export PYTHONPATH=src
python scripts/day13_ingest_chunks.py

## Search
python scripts/day13_search_chunks.py
