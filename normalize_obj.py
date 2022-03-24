import open3d as o3d
import argparse, sys, os, time
import numpy as np

def normalize_obj(file_path, out_path):
    obj = o3d.io.read_triangle_mesh(file_path)
    scale = max((obj.get_max_bound() - obj.get_min_bound())/2)
    center = obj.get_center()
    obj = obj.translate(-center)
    obj = obj.scale(1/scale, np.zeros((3,1)))
    o3d.io.write_triangle_mesh(out_path, obj)

if __name__ == '__main__':
    output_folder='./norm_part'
    model_dir = './partnet/'

    model_ids = os.listdir(model_dir)
    tot_id = 0
    for index, model_id in enumerate(model_ids):
        objs_dir = os.path.join(model_dir, model_id, "objs") 
        objs = os.listdir(objs_dir)
        for obj in objs:
            print(tot_id)
            save_dir = os.path.join(output_folder, '%05d'%tot_id)
            if os.path.exists(save_dir) == False:
                obj_file = os.path.join(objs_dir, obj)
                os.makedirs(save_dir)
                norm_obj_path = os.path.join(save_dir, '%05d.obj'%(tot_id))
                normalize_obj(obj_file, norm_obj_path)
            tot_id += 1