

# from utils import save_trajectory
def save_trajectory(trajectory, filename, with_time=True):
    with open(filename, 'w') as traj_file:
        if with_time:
            traj_file.writelines('{time} {r00} {r01} {r02} {t0} {r10} {r11} {r12} {t1} {r20} {r21} {r22} {t2}\n'.format(
                time=repr(t),
                r00=repr(r00),
                r01=repr(r01),
                r02=repr(r02),
                t0=repr(t0),
                r10=repr(r10),
                r11=repr(r11),
                r12=repr(r12),
                t1=repr(t1),
                r20=repr(r20),
                r21=repr(r21),
                r22=repr(r22),
                t2=repr(t2)
            ) for t, r00, r01, r02, t0, r10, r11, r12, t1, r20, r21, r22, t2 in trajectory)
        else:
            traj_file.writelines('{r00} {r01} {r02} {t0} {r10} {r11} {r12} {t1} {r20} {r21} {r22} {t2}\n'.format(
                r00=repr(r00),
                r01=repr(r01),
                r02=repr(r02),
                t0=repr(t0),
                r10=repr(r10),
                r11=repr(r11),
                r12=repr(r12),
                t1=repr(t1),
                r20=repr(r20),
                r21=repr(r21),
                r22=repr(r22),
                t2=repr(t2)
            ) for t, r00, r01, r02, t0, r10, r11, r12, t1, r20, r21, r22, t2 in trajectory)
            
