from eye_tracker import track_eye
from head_pose_estimation import detect_head_pose
from mouth_opening_detector import mouth_opening_detector
from person_and_phone import detect_phone_and_person
from multiprocessing import Process

from utilities import send_videos_to_backend


if __name__ == '__main__':
    p1 = Process(target=track_eye, args=(0,))
    p2 = Process(target=detect_head_pose, args=(0,))
    p3 = Process(target=mouth_opening_detector, args=(0,))
    p4 = Process(target=detect_phone_and_person, args=(0,))
    p5 = Process(target=send_videos_to_backend, args=('./recordings',"https://phpstack-1245936-4719805.cloudwaysapps.com/backend/api/v1/candidate/exam/proctor-assets",{'candidate_id': '444444444444test', 'ip_address':'192.168.92.1'}))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
   # p5.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    # p5.join()
   