
scores = [45, 80, 65, 90, 35]

passed = [s for s in scores if s >= 60]
failed = [s for s in scores if s < 60]

print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Pass count: {len(passed)}")
