(define (problem high_level)
  (:domain high_level_domain)
  (:objects
     
     home bedroom outside living_room - Landmark
     med_r1 med_r2 med_r3 med_r4 food_r1 food_r2 food_r3 food_r4 - OneReminderProtocol
     nathan - Person
     night_video - NightVideo
     t1 - Time  ;;t2 t3 t4 t5

    ;; for low level
    reminder_1_msg reminder_2_msg voice_msg - Msg
    first_reminder second_reminder - ReminderAction
    caregiver_call - CallAction
    voice_command - VoiceAction

  )
  (:init
      ;;(time_for_night_video night_video)
      (priority_1)
      (visible_location home)
      (visible_location living_room)
      (visible_location bedroom)
      (check_location_wakeup living_room)
      (check_location_wakeup home)
      (not_visible_location outside)
      

  )
  (:goal (and (success)  ) )
)