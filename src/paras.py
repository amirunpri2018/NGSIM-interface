import datetime

NUM_COLS = 25

GLB_vehID_colidx = 0
GLB_frmID_colidx = 1
GLB_totfrm_colidx = 2
GLB_glbtime_colidx = 3
GLB_locx_colidx = 4
GLB_locy_colidx = 5
GLB_glbx_colidx = 6
GLB_glby_colidx = 7
GLB_vehlen_colidx = 8
GLB_vehwid_colidx = 9
GLB_vehcls_colidx = 10
GLB_vehspd_colidx = 11
GLB_vehacc_colidx = 12
GLB_laneID_colidx = 13
GLB_Ozone_colidx = 14
GLB_Dzone_colidx = 15
GLB_interID_colidx = 16
GLB_sectID_colidx =17
GLB_dirc_colidx = 18
GLB_mov_colidx = 19
GLB_pred_colidx = 20
GLB_follow_colidx = 21
GLB_shead_colidx = 22 
GLB_thead_colidx = 23
GLB_loc_colidx = 24



timezone_dict = dict()
timezone_dict['i-80'] = 'America/Los_Angeles'


GLOB_IMPUTE_K_SWEEP = [5, 10, 15]