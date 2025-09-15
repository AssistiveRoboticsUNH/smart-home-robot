(define (domain high_level_domain)

(:requirements
  :strips
  :typing
)

(:types
  OneReminderProtocol
  Landmark
  Time
  Person

  ;; low level from types in low level domain
  ;; was added because kb doesnt store intermediate success for the low level
  ;; this enable the low level to continue form where it stopped by adding to high level
  ;; kb only keeps predicates that are part of the high level
    Msg
    ReminderAction
    CallAction
    VoiceAction
)

(:predicates
  (started)

  (robot_at ?lmr - Landmark)
  (person_at ?t - Time ?p - Person ?lmp - Landmark)
  (person_currently_at ?p - Person ?lmp - Landmark)

  (visible_location ?lmp - Landmark)
  (not_visible_location ?lmp - Landmark)
  (check_location_wakeup ?lmp - Landmark)
  
  ;; one reminder
  (one_reminder_protocol_enabled ?oner - OneReminderProtocol)
  (time_for_one_reminder ?oner - OneReminderProtocol)
  (already_reminded_one_reminder ?oner - OneReminderProtocol)


  (low_level_failed)

  ;; priority
  ;; all protocols should have a priority higher than that of idle
  (priority_1)
  (priority_2)
  (priority_3)
  (priority_4)
  (priority_5)
  (priority_6)
 

  (dont_use_shutdown)
  (success)

  ;; for low level domain
  ;; these should include actions that need to be done only once
  (executed_reminder ?a - ReminderAction)
  (executed_call ?c - CallAction)
  (executed_voice ?a - VoiceAction)
  (message_given ?m - Msg)
)

(:action MoveToLandmark
	:parameters (?from - Landmark ?to - Landmark)
	:precondition (and
	                (robot_at ?from)
	                (started)
	                (visible_location ?from)
                    (visible_location ?to)
                    (not (not_visible_location ?from))
                    (not (not_visible_location ?to))
	          )
	:effect (and (robot_at ?to) (not (robot_at ?from)) )
)


(:action ChangePriority_1_2
	:parameters ()
	:precondition (and
	    (priority_1)
		)
	:effect (and (priority_2) (not (priority_1)))
)
(:action ChangePriority_2_3
	:parameters ()
	:precondition (and
	    (priority_2)
		)
	:effect (and (priority_3) (not (priority_2)))
)
(:action ChangePriority_3_4
	:parameters ()
	:precondition (and
	    (priority_3)
		)
	:effect (and (priority_4) (not (priority_3)))
)
(:action ChangePriority_4_5
	:parameters ()
	:precondition (and
	    (priority_4)
		)
	:effect (and (priority_5) (not (priority_4)))
)

(:action ChangePriority_5_6
	:parameters ()
	:precondition (and
	    (priority_5)
		)
	:effect (and (priority_6) (not (priority_5)))
)

;; to start ros and navigation before the protocol
(:action StartROS
	:parameters ()
	:precondition (;;and
        ;;(priority_2)
	    ;; will be triggered before it starts a protocol
		)
	:effect (and
                (started)
                ;;(not (priority_2))
          )
)

(:action StartOneReminderProtocol
	:parameters (?o - OneReminderProtocol ?p - Person ?cur - Landmark ?dest - Landmark)
	:precondition (and
	  ;; all protocols should have a priority higher than that of idle
	  (priority_3)
      (time_for_one_reminder ?o)

      (visible_location ?dest)
      (visible_location ?cur)

      (person_currently_at ?p ?cur)
      ;;(robot_at ?cur)

      (not (already_reminded_one_reminder ?o))

      (forall (?o - OneReminderProtocol) (not (one_reminder_protocol_enabled ?o)) )
      (started)
		)
	:effect (and
	        (success)
            ;;(started)
            (not (priority_2))
            (one_reminder_protocol_enabled ?o)
            (not (low_level_failed))
            ;; for every protocol in types it has to have a forall to disable other protocols before starting this one
          )
)

(:action ContinueOneReminderProtocol
	:parameters (?o - OneReminderProtocol)
	:precondition (and
	    (priority_2)
	    (not (low_level_failed))
      (time_for_one_reminder ?o)
      (not (already_reminded_one_reminder ?o))
      (one_reminder_protocol_enabled ?o)
		)
	:effect (and (success) (not (priority_3)) )
)


(:action Idle
	:parameters ()
	:precondition (and
	    (priority_6)
		)
	:effect (and (success)
	             (not (priority_6))
	             (not (low_level_failed))
	            ;; for every protocol in types it has to have a forall to disable other protocols before starting this one
                (forall (?one_reminder_protocol - OneReminderProtocol) (not (one_reminder_protocol_enabled ?one_reminder_protocol)) )
          )
)
;; shutdown is supposed to stop ros2 processes
;; it should try to dock if it is not docked
;; triggered when there should be protocol and it has been done

(:action Shutdown
	:parameters ()
	:precondition
	    (and
	        (started)
	        ;; has to be higher priority than idle
            (priority_5)

            ;; CANT SHUTDOWN IF time to do something is true and
            ;; all predicates indicating that they it is done are false
            ;; give F in such case

            ;; need to add a forall for every protocol objects in problem
            ;;; 1
            ;;; forall would give false if one is F

            ;; ADD CHANGES HERE
            (forall (?oner - OneReminderProtocol)
                (not
                    (and
                        (time_for_one_reminder ?oner)
                        (not (already_reminded_one_reminder ?oner))
                    )
                )
            )
	    )
	:effect (and (success)
	            (not (priority_5))
                (not (low_level_failed))
                (not started)
          )
)
)