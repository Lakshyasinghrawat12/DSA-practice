# Use a Set for Tracking:

- Use a set to store elements from one of the arrays.


# Find the Intersection:

- Iterate through the second array and check if each element is in the set from the first array. If it is, add it to the result list and remove it from the set to ensure each element is unique.

**Time Complexity:** O(n + m), where n is the length of nums1 and m is the length of nums2. This is because you go through both arrays once.
**Space Complexity:** O(min(n, m)), where you use space for storing elements in the set from the smaller array.