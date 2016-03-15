#include <time.h>
#include <stdlib.h>
#include <stdio.h>

int main() {
    time_t current_time;
    char* c_time_string;
    current_time = time(NULL);
    /* Convert to local time format. */
    c_time_string = ctime(&current_time);
    printf("%s", c_time_string);
    return 0;
}
