## Some Important Concepts:

1. "Zero-time activities": Activities that happen at the same clock time. An activity set can have multiple chain of activities. If such sub-activities are part of two different chains, then order of execution must be carefully defined for ensuring the correct outcome.
2. "Conditional Event": An event that must lay dormant until the condition preventing the outcome changes. A seperate list of conditional events can be made - "ready list". The list needs to be scanned after every condition change.
	* The ready list must be re-iterated after each conditional release to maintain the priority order of simultaneous events.
3. All events that can be blocked represent **Conditional events**.
4. 