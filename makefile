# Compiler and flags
CC = gcc
CFLAGS = -Wall -Wextra -g

# Source files
SRCS = day1/day1.c

# Object files
OBJS = $(SRCS:.c=.o)

# Executable
TARGET = myprogram

# Default target
all: $(TARGET)

# Compile source files into object files
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Link object files into executable
$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) $^ -o $@

# Clean up object files and executable
clean:
	rm -f $(OBJS) $(TARGET)
