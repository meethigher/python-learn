import time
import json
import psycopg2
import sys

# Configuration file path
CONFIG_FILE = "config.json"


def load_config():
    """Load configuration from JSON file"""
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Failed to load config file: {e}")
        sys.exit(1)


def benchmark_query(db_config, sql_query, n):
    """Execute SQL query n times and record execution time"""
    times = []

    # Record start time
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    overall_start = time.perf_counter()

    try:
        with psycopg2.connect(**db_config) as conn:
            with conn.cursor() as cur:
                for _ in range(n):
                    query_start = time.perf_counter()
                    cur.execute(sql_query)  # Execute SQL query
                    cur.fetchall()  # Fetch results to avoid lazy execution
                    elapsed_time = time.perf_counter() - query_start
                    times.append(elapsed_time)

        # Record end time
        overall_end = time.perf_counter()
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # Calculate statistics
        avg_time = sum(times) / len(times)
        max_time = max(times)
        min_time = min(times)
        total_time = overall_end - overall_start

        print(f" SQL executed {n} times")
        print(f"   Start time: {start_time}")
        print(f"   End time: {end_time}")
        print(f"   Total execution time: {total_time:.6f} seconds")
        print(f"   Average query time: {avg_time:.6f} seconds")
        print(f"   Max query time: {max_time:.6f} seconds")
        print(f"   Min query time: {min_time:.6f} seconds")

    except Exception as e:
        print(f"❌ Failed to execute SQL: {e}")
        sys.exit(1)


if __name__ == "__main__":
    config = load_config()
    benchmark_query(config["database"], config["query"], config["iterations"])
