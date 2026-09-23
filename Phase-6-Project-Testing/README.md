# Phase 6 – Project Testing

## 1. Testing Overview

EduGenie is tested to verify that the main learning features work correctly and provide useful AI-generated responses.

## 2. Features Tested

1. Educational Question Answering
2. Concept Explanation
3. Quiz Generation
4. Text Summarization
5. Personalized Learning Recommendations

## 3. Backend Testing

The FastAPI endpoints are tested to ensure that requests are received correctly and appropriate responses are returned.

Main endpoints:

- `/qa`
- `/explain`
- `/quiz`
- `/summarize`
- `/learn/recommendations`

## 4. Functional Testing

Test cases include:

- Entering a valid educational question
- Requesting an explanation of a topic
- Generating a quiz
- Providing educational text for summarization
- Requesting a personalized learning path

## 5. Expected Result

Each valid request should return an AI-generated response through the EduGenie web interface.

## 6. Error Testing

The application should handle empty inputs and invalid requests without crashing.

## 7. Testing Conclusion

The testing process verifies the major EduGenie functions and confirms that the application is ready for demonstration.
