# To-Do-List-Management-System

A command-line task management application built in Python. It allows users to track tasks assign priorities and categories manage completion statuses, search entries and view productivity metrics all through an interactive terminal interface.

---

## Overview

The To-Do List Management System is a memory-stored CLI application designed to help users organize their daily workload. It features task lifecycle management including creation, inline updates, filtering by completion status case-insensitive keyword searching and real-time productivity statistics.

---

## Features

### 1. Task Creation & Categorization

- Task Entry: Input a title and optional task description.

- Priority Levels: Assign High, Medium or Low priority (defaults to Medium on invalid selection).

- Categories: Group tasks into College, Personal, Work or Other.

- Default Status: Automatically initializes all tasks with a Pending status.

### 2. Viewing & Filtering Options

- View All Tasks: Display a list of entries with title, description, priority, category and status.

- Pending Tasks: Filter and view open/incomplete tasks.

- Completed Tasks: Filter and view only finalized tasks.

### 3. Search & Task Operations

- Search: Search for tasks by title using case- partial keyword matching.

- Update Task: Select an existing task by index to update its title, description or priority level.

- Mark Complete: Instantly change any task status from Pending to Completed.

- Delete Task: Remove tasks, by index with a built-in (yes/no) confirmation prompt to prevent accidental loss.

### 4. Productivity Analytics

- Task Statistics: Summarizes overall performance showing tasks, completed tasks, pending tasks and overall percentage completion rate.

---

## Technologies Used

- Language: Python 3.x[cite: 3]

- Storage: In-memory collection (list of dict objects)[cite: 3]

- Dependencies: None (Uses Python built-in standard features only)[cite: 3]

---

## Project Structure

```text

todo_list_system/

├── README.md                          # Project documentation

├── Final Vityarthi Project Done.py    # Main CLI application script

```
