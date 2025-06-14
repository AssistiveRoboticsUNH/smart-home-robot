(define (problem shr_domain_problem)
(:domain shr_domain)
(:objects
	 w5 - WaitAction
	 w3 - WaitAction
	 w4 - WaitAction
	 w2 - WaitAction
	 caregiver_call - CallAction
	 call_caregiver_msg - Msg
	 second_reminder - ReminderAction
	 na2 - NoAction
	 reminder_1_msg - Msg
	 t2 - Time
	 bedroom - Landmark
	 nathan - Person
	 t1 - Time
	 home - Landmark
	 outside - Landmark
	 living_room - Landmark
	 na3 - NoAction
	 reminder_2_msg - Msg
	 w1 - WaitAction
	 voice_msg - Msg
	 voice_command - VoiceAction
	 na1 - NoAction
	 t4 - Time
	 t3 - Time
	 first_reminder - ReminderAction
	 t5 - Time
)
(:init
	(noaction_person_location_constraint na3 nathan outside)
	(noaction_person_location_constraint na1 nathan outside)
	(noaction_person_location_constraint na2 nathan outside)
	(wait_not_person_location_constraint t1 nathan outside)
	(wait_not_person_location_constraint t2 nathan outside)
	(wait_not_person_location_constraint t3 nathan outside)
	(wait_not_person_location_constraint t4 nathan outside)
	(wait_not_person_location_constraint t5 nathan outside)
	(valid_reminder_message first_reminder reminder_1_msg)
	(valid_reminder_message second_reminder reminder_2_msg)
	(message_given_success reminder_2_msg)
	(reminder_blocks_reminder first_reminder second_reminder)
	(DetectTakingMedicine_enabled)
	(wait_robot_location_constraint t1 home)
	(wait_robot_location_constraint t2 home)
	(wait_robot_location_constraint t3 home)
	(wait_robot_location_constraint t4 home)
	(robot_at living_room)
	(medicine_taken_success)
	(person_at t1 nathan living_room)
	(traversable home bedroom)
	(traversable bedroom living_room)
	(traversable living_room bedroom)
	(traversable home living_room)
	(traversable living_room home)
	(traversable bedroom home)
	(reminder_person_not_taking_medicine_constraint first_reminder nathan)
	(reminder_person_not_taking_medicine_constraint second_reminder nathan)
	(current_time t1)
	(same_location_constraint)
	(DetectPerson_enabled)
	(person_currently_at nathan living_room)
	(GiveReminder_enabled)
	(next_time t4 t5)
	(next_time t3 t4)
	(next_time t2 t3)
	(next_time t1 t2)
	(unknown (person_at t5 nathan outside))
	(unknown (person_at t5 nathan bedroom))
	(unknown (person_at t5 nathan living_room))
	(unknown (person_at t4 nathan outside))
	(unknown (person_at t4 nathan bedroom))
	(unknown (person_at t4 nathan living_room))
	(unknown (person_at t3 nathan outside))
	(unknown (person_at t3 nathan bedroom))
	(unknown (person_at t3 nathan living_room))
	(unknown (person_at t2 nathan outside))
	(unknown (person_at t2 nathan bedroom))
	(unknown (person_at t2 nathan living_room))
	(oneof (person_at t2 nathan living_room) (person_at t2 nathan bedroom) (person_at t2 nathan outside))
	(oneof (person_at t3 nathan living_room) (person_at t3 nathan bedroom) (person_at t3 nathan outside))
	(oneof (person_at t4 nathan living_room) (person_at t4 nathan bedroom) (person_at t4 nathan outside))
	(oneof (person_at t5 nathan living_room) (person_at t5 nathan bedroom) (person_at t5 nathan outside))
)
(:goal
(success))
)