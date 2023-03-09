#include<iostream>
#include<string>



/* overarching movement variables */
// Q: Are we sweeping left or right?

/* move forward */
// get distance
// determine if there is space to move
    // yes -> calculate the space needed to move

    // no -> turn (which direction?)




/* turn */



using namespace std;



int get_total_forward_distance() {
    int distance;
    return distance; /* code for getting the distance from the sensors */
}


bool there_is_space_to_move(int distance, int limit) {
    if (distance > limit) // in cm
        return true;
    else {
        return false;
    }

}


int calculate_forward_clearance(int limit) {
    int distance; 
    /* code for getting the distance from the sensors */
    return distance-limit;
}

void move_forward(int distance) {
    /* v(motor power in %) = length of 1 rev of treads/time to complete one revolution at power % */
    // start a table of values
}

void turn_left_90() {
    // rover motors move in opposite directions
    // right -> forward
    // left -> reverse
}
void turn_right_90() {
    // rover motors move in opposite directions
    // right -> reverse
    // left -> forward
}

void move_turn(string left_or_right) {
    // Needs a more elegant solution, but a working solution comes first.


    // turn 90 degrees
        // but which direction? It must be specified.
    int width_of_rover = 40;    // cm
    if (left_or_right == "left") {
        turn_left_90();
        if (get_total_forward_distance() >= width_of_rover) {
            move_forward(width_of_rover);
            turn_left_90();
        }
        else {
            turn_left_90();
        }

    }
    else {
        turn_right_90();
        if (get_total_forward_distance() >= width_of_rover) {
            move_forward(width_of_rover);
            turn_right_90();
        }
        else {
            turn_right_90();
        }

    }
}


int main() {

    int t = 1000;                                            // time in s
    string room_sweep_direction = "left";                    // "left" or "right"        // quotes are needed
    int minimum_allowable_distance_from_obstacle = 20;       // distance in cm

    while (t > 0) {

  
        if (get_total_forward_distance() > minimum_allowable_distance_from_obstacle) {
            move_forward(get_total_forward_distance() - minimum_allowable_distance_from_obstacle);
        }
        else {
            move_turn(room_sweep_direction);
        }

    }

    return 0;
}