// Mars lander simulator
// Version 1.11
// Mechanical simulation functions
// Gabor Csanyi and Andrew Gee, August 2019

// Permission is hereby granted, free of charge, to any person obtaining
// a copy of this software and associated documentation, to make use of it
// for non-commercial purposes, provided that (a) its original authorship
// is acknowledged and (b) no modified versions of the source code are
// published. Restriction (b) is designed to protect the integrity of the
// exercise for future generations of students. The authors would be happy
// to receive any suggested modifications by private correspondence to
// ahg@eng.cam.ac.uk and gc121@eng.cam.ac.uk.

#include "lander.h"
#include <fstream>

void autopilot (void)
  // Autopilot to adjust the engine throttle, parachute and attitude control
{
  double Kh, error, Kp, p_out, delta, altitude;

  // setting constants
  Kh = 0.05;
  Kp = 0.8;
  delta = 0.4;
  altitude = position.abs() - MARS_RADIUS;

  // equations
  error = -(0.5 + Kh*altitude - velocity.abs());
  p_out = Kp * error;
  
  // parachute
  if ((altitude < 5000) && safe_to_deploy_parachute()) {
      parachute_status = DEPLOYED;
  }
  

  // throttle control

 if (p_out <= (-delta)) {
    throttle = 0;
  }
  else if ( (p_out > (-delta)) && (p_out < (1 - delta))) {
    throttle = delta + p_out;
  }
  else if ( p_out >= (1-delta)) {
    throttle = 1;
  }
  else {
    cout << "Error with throttle control." << endl;
  }


}

void numerical_dynamics (void)
  // This is the function that performs the numerical integration to update the
  // lander's pose. The time step is delta_t (global variable).
{
  double d, a_gravity_scalar, a_drag_scalar, altitude;
  vector3d a_gravity, a_thrust, a_drag, a, thr, new_position;
  double lander_mass;
  static vector3d previous_position;
  vector<double> t_list;

  thr = thrust_wrt_world();
  d = atmospheric_density(position);
  altitude = position.abs() - MARS_RADIUS;


  // function of lander's mass
  lander_mass = UNLOADED_LANDER_MASS + (fuel*FUEL_CAPACITY*FUEL_DENSITY);

  // calculate gravity
  a_gravity_scalar = GRAVITY * MARS_MASS / (position.abs2());
  a_gravity = - a_gravity_scalar * position.norm();

  // calculate thrust
  a_thrust = thr / (lander_mass);
  
  // calculate drag
 if (parachute_status == DEPLOYED){
      a_drag_scalar = 0.5 * d * DRAG_COEF_LANDER * (PI * LANDER_SIZE * LANDER_SIZE) * velocity.abs2()+  5 * 0.5 * d * DRAG_COEF_CHUTE * ((2.0*LANDER_SIZE)*(2.0*LANDER_SIZE)) * velocity.abs2();
    }
 else {
      a_drag_scalar = 0.5 * d * DRAG_COEF_LANDER * (PI * LANDER_SIZE * LANDER_SIZE) * velocity.abs2();
    }
  a_drag = - (a_drag_scalar/lander_mass) * velocity.norm();

  a = a_gravity + a_thrust + a_drag;

  // vertlet integration
  if (simulation_time <= 0) {
    previous_position = position;
    position = position + velocity * delta_t;
    velocity = velocity + a * delta_t;
  }
  else {
    new_position = 2*position - previous_position + a * (delta_t * delta_t);
    velocity = (new_position - previous_position) / (2*delta_t);

    previous_position = position;
    position = new_position;

  }

  t_list.push_back(simulation_time);
  //cout << "Time is: " << simulation_time << endl;
  //cout << "Altitude is: " << altitude << endl;
  if (simulation_time > 205 && simulation_time < 205 + delta_t) {
    ofstream fout;
    fout.open("trajectories.txt");
    if (fout) { // file opened successfully
      for (int i = 0; i < t_list.size(); i = i + 1) {
	fout << t_list[i] << endl;
      }
    } else { // file did not open successfully
      cout << "Could not open trajectory file for writing" << endl;
    }
  }

  /*
  t_list.push_back(simulation_time);
  cout << simulation_time << endl;
  if (simulation_time == 200) {
    for (i = 0; i < t_list.size() ; i = i + delta_t) {
      cout << t_list[i] << endl;
    }
    cout << "working" << endl;
  }
  */
  
    

  // Here we can apply an autopilot to adjust the thrust, parachute and attitude
  if (autopilot_enabled) autopilot();

  // Here we can apply 3-axis stabilization to ensure the base is always pointing downwards
  if (stabilized_attitude) attitude_stabilization();
}

void initialize_simulation (void)
  // Lander pose initialization - selects one of 10 possible scenarios
{
  // The parameters to set are:
  // position - in Cartesian planetary coordinate system (m)
  // velocity - in Cartesian planetary coordinate system (m/s)
  // orientation - in lander coordinate system (xyz Euler angles, degrees)
  // delta_t - the simulation time step
  // boolean state variables - parachute_status, stabilized_attitude, autopilot_enabled
  // scenario_description - a descriptive string for the help screen

  scenario_description[0] = "circular orbit";
  scenario_description[1] = "descent from 10km";
  scenario_description[2] = "elliptical orbit, thrust changes orbital plane";
  scenario_description[3] = "polar launch at escape velocity (but drag prevents escape)";
  scenario_description[4] = "elliptical orbit that clips the atmosphere and decays";
  scenario_description[5] = "descent from 200km";
  scenario_description[6] = "";
  scenario_description[7] = "";
  scenario_description[8] = "";
  scenario_description[9] = "";

  switch (scenario) {

  case 0:
    // a circular equatorial orbit
    position = vector3d(1.2*MARS_RADIUS, 0.0, 0.0);
    velocity = vector3d(0.0, -3247.087385863725, 0.0);
    orientation = vector3d(0.0, 90.0, 0.0);
    delta_t = 0.1;
    parachute_status = NOT_DEPLOYED;
    stabilized_attitude = false;
    autopilot_enabled = false;
    break;

  case 1:
    // a descent from rest at 10km altitude
    position = vector3d(0.0, -(MARS_RADIUS + 10000.0), 0.0);
    velocity = vector3d(0.0, 0.0, 0.0);
    orientation = vector3d(0.0, 0.0, 90.0);
    delta_t = 0.1;
    parachute_status = NOT_DEPLOYED;
    stabilized_attitude = true;
    autopilot_enabled = true;

    break;

  case 2:
    // an elliptical polar orbit
    position = vector3d(0.0, 0.0, 1.2*MARS_RADIUS);
    velocity = vector3d(3500.0, 0.0, 0.0);
    orientation = vector3d(0.0, 0.0, 90.0);
    delta_t = 0.1;
    parachute_status = NOT_DEPLOYED;
    stabilized_attitude = false;
    autopilot_enabled = false;
    break;

  case 3:
    // polar surface launch at escape velocity (but drag prevents escape)
    position = vector3d(0.0, 0.0, MARS_RADIUS + LANDER_SIZE/2.0);
    velocity = vector3d(0.0, 0.0, 5027.0);
    orientation = vector3d(0.0, 0.0, 0.0);
    delta_t = 0.1;
    parachute_status = NOT_DEPLOYED;
    stabilized_attitude = false;
    autopilot_enabled = false;
    break;

  case 4:
    // an elliptical orbit that clips the atmosphere each time round, losing energy
    position = vector3d(0.0, 0.0, MARS_RADIUS + 100000.0);
    velocity = vector3d(4000.0, 0.0, 0.0);
    orientation = vector3d(0.0, 90.0, 0.0);
    delta_t = 0.1;
    parachute_status = NOT_DEPLOYED;
    stabilized_attitude = false;
    autopilot_enabled = false;
    break;

  case 5:
    // a descent from rest at the edge of the exosphere
    position = vector3d(0.0, -(MARS_RADIUS + EXOSPHERE), 0.0);
    velocity = vector3d(0.0, 0.0, 0.0);
    orientation = vector3d(0.0, 0.0, 90.0);
    delta_t = 0.1;
    parachute_status = NOT_DEPLOYED;
    stabilized_attitude = true;
    autopilot_enabled = true;
    break;

  case 6:
    break;

  case 7:
    break;

  case 8:
    break;

  case 9:
    break;

  }
}

/*
int main() {
   // Write the trajectories to file
 ofstream fout;
 fout.open("trajectories.txt");
 if (fout) { // file opened successfully
   for (int i = 0; i < h_list.size(); i = i + 1) {
     fout << h_list[i] << " " << v_list[i] << endl;
   }
 } else { // file did not open successfully
 cout << "Could not open trajectory file for writing" << endl;
 }

*/

