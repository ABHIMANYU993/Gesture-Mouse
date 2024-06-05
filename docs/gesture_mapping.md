# Hand Gesture Mapping Reference

The virtual mouse maps specific hand configurations and finger distances to OS-level mouse actions:

| Hand Gesture / Configuration | Visual Overlay Action | Simulated System Action |
| :--- | :--- | :--- |
| **Only Index Finger Open** | Bounding box on index tip | Cursor Movement |
| **Index + Middle Fingers Open (Distance < 50px)** | Green dot between tips | Mouse Left Click |
| **Index + Thumb Open (Distance 30px - 120px)** | Circle between tips | Zoom In (`Ctrl + Scroll Up`) |
| **Index + Thumb Open (Distance 120px - 200px)** | Circle between tips | Zoom Out (`Ctrl + Scroll Down`) |
| **All Fingers Closed (Fist)** | None | Scroll Up |
| **Only Thumb Finger Open** | None | Scroll Down |
| **Only Pinky Finger Open** | None | Mouse Right Click |
| **Pinky + Index Fingers Open** | None | Scroll Right (Horizontal) |
| **Pinky + Index + Thumb Open** | None | Scroll Left (Horizontal) |
