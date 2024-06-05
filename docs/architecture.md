# Gesture Mouse System Architecture

This document details the system design, data flow, and interactions between the components of the Gesture Interaction Virtual Mouse.

## High-Level System Overview
The system follows a modular architectural pattern consisting of three core layers:
1. Perception Layer (Webcam Capture via OpenCV)
2. Processing & Tracking Layer (MediaPipe Hands pipeline)
3. Input Simulation Layer (autopy, pyautogui, pynput, and mouse)

## Processing Pipeline Flow
```mermaid
graph TD
    A[Webcam Video Capture] -->|BGR Frame| B[Image Processing & RGB Conversion]
    B -->|RGB Frame| C[MediaPipe Hands Detection Pipeline]
    C -->|Hand Landmarks & BBoxes| D[Gesture Interpretation Layer]
    D -->|Coordinates & Distance Calculation| E[Input Simulation Layer]
    E -->|PyAutoGUI / autopy / pynput / mouse| F[OS GUI System Actions]
```
