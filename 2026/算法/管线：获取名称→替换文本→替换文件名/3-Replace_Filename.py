import os
import shutil

# ==========================
# 1. 字典（请放入你的完整字典）
# ==========================
mapping = {
    "链路弯": "LinkBend",
    "孔": "Hole",
    "中间部纵梁加强": "MiddleLongitudinalBeamReinforcement",
    "培林总成": "BearingAssembly",
    "横梁": "Crossbeam",
    "电机梁": "MotorBeam",
    "左挡板": "LeftBaffle",
    "云台定子固定横": "GimbalStatorFixingCross",
    "云台安装件": "GimbalMount",
    "电机尾": "MotorTail",
    "大臂对侧": "LargeArmOppositeSide",
    "改": "Modify",
    "上": "Upper",
    "合页一半": "HingeHalfOne",
    "大臂垫块": "LargeArmSpacer",
    "后挂载板": "RearMountingPlate",
    "前": "Front",
    "外圈垫板": "OuterRingSpacer",
    "图传模块": "ImageTransmissionModule",
    "碗组连接": "BowlSetConnection",
    "拨盘挡边": "DialBaffleEdge",
    "减比": "ReductionRatio",
    "土字": "TCharacter",
    "弹舱下板": "AmmunitionBayBottomPlate",
    "新图传固定架": "NewImageTransmissionFixingFrame",
    "标件": "StandardPart",
    "新肩竖侧保护板": "NewShoulderVerticalSideGuardPlate",
    "拨盘电机安装座": "DialMotorMount",
    "连接": "Connection",
    "飞坡导轮安装加长": "RampGuideWheelMountingExtension",
    "防撞杠侧面加固": "BumperSideReinforcement",
    "导轮": "GuideWheel",
    "直流无刷减速电机": "DCOutrunnerGearedMotor",
    "电机内安装板": "MotorInnerMountingPlate",
    "前后防撞杠": "FrontRearBumper",
    "合页另一半": "HingeHalfOther",
    "拨盘底部壁面": "DialBottomWallSurface",
    "电机头": "MotorHead",
    "车架完整": "ChassisComplete",
    "摩擦轮": "FrictionWheel",
    "装甲板垫块": "ArmorPlateSpacer",
    "电池架左侧安装板": "BatteryRackLeftMountingPlate",
    "轴基座轴承内圈垫圈": "AxleBaseBearingInnerRingWasher",
    "长": "Long",
    "大疆电池座": "DJIBatterySeat",
    "轴电机安装板": "AxleMotorMountingPlate",
    "垫高板": "RaisingPlate",
    "裁判系统测速模块": "RefereeSystemSpeedMeasurementModule",
    "推力轴承": "ThrustBearing",
    "新前上保护板": "NewFrontUpperGuardPlate",
    "飞坡导轮连接板": "RampGuideWheelConnectionPlate",
    "纵梁端口": "LongitudinalBeamPort",
    "电机梁内嵌件内四": "MotorBeamInnerInsertInnerFour",
    "电机腰": "MotorWaist",
    "电池": "Battery",
    "防撞导轮固定板": "AntiCollisionGuideWheelFixingPlate",
    "轴承加强外壳": "BearingReinforcementCasing",
    "打印件": "PrintedPart",
    "摩擦轮弹道": "FrictionWheelTrajectory",
    "腿竖侧保护板": "LegVerticalSideGuardPlate",
    "碗组": "BowlSet",
    "飞坡导轮转接件": "RampGuideWheelAdapter",
    "新版": "NewVersion",
    "弹舱中板": "AmmunitionBayMiddlePlate",
    "拨盘出弹导轨": "DialEjectionGuideRail",
    "带后盖": "WithRearCover",
    "铜嵌件": "CopperInsert",
    "轮组连接": "WheelSetConnection",
    "直流无刷减速电": "DCOutrunnerGeared",
    "拨盘底板": "DialBasePlate",
    "电容主板盒盖": "CapacitorMainBoardBoxCover",
    "中间部纵梁": "MiddleLongitudinalBeam",
    "弹舱上板": "AmmunitionBayUpperPlate",
    "垫块": "Spacer",
    "板材": "SheetMaterial",
    "侧面保护壳": "SideProtectiveShell",
    "相机电机连接件": "CameraMotorConnector",
    "安装件": "MountingPart",
    "拨盘上部壁面": "DialUpperWallSurface",
    "小臂": "SmallArm",
    "碗组垫块": "BowlSetSpacer",
    "直流无刷电机": "DCOutrunnerMotor",
    "导电滑环小端固定件": "ConductiveSlipRingSmallEndFixingPart",
    "下底": "BottomBase",
    "轴承扣": "BearingBuckle",
    "新炮台前挡": "NewTurretFrontBaffle",
    "摩擦轮包胶": "FrictionWheelRubberCoating",
    "电池架右侧安装板": "BatteryRackRightMountingPlate",
    "内圈压板": "InnerRingPressurePlate",
    "电控安装板垫高": "ElectronicControlMountingPlateRaised",
    "外": "Outer",
    "电管安装板": "CableManagementMountingPlate",
    "顶板": "TopPlate",
    "双枪测速安装铝件": "DualGunSpeedMeasurementAluminumMount",
    "轮轴加工": "WheelAxleMachining",
    "电池保护盖": "BatteryProtectiveCover",
    "步兵交叉滚子轴承垫": "InfantryCrossedRollerBearingPad",
    "前后保护盖上": "FrontRearProtectiveCoverUpper",
    "腿斜下保护板": "LegDiagonalLowerGuardPlate",
    "盖板": "CoverPlate",
    "二版": "VersionTwo",
    "齿轮保护": "GearProtection",
    "挡板": "Baffle",
    "中挡板": "MiddleBaffle",
    "支撑架": "SupportFrame",
    "加强输出端": "ReinforcedOutputEnd",
    "电机联轴器": "MotorCoupling",
    "弹链转轴连接": "AmmoBeltRotatingShaftConnection",
    "电管垫柱": "CableManagementSpacer",
    "云台基板": "GimbalBasePlate",
    "新切枪板": "NewCuttingGunPlate",
    "转接件": "Adapter",
    "电容模块盒盖": "CapacitorModuleBoxCover",
    "侧面防撞杠": "SideBumper",
    "法兰端": "FlangeEnd",
    "路": "Path",
    "侧弹道": "SideTrajectory",
    "屁股": "RearEnd",
    "电机梁内嵌件内四限位": "MotorBeamInnerInsertInnerFourLimit",
    "横梁加强": "CrossbeamReinforcement",
    "型孔联轴器": "ShapedHoleCoupling",
    "电容模块盒底部": "CapacitorModuleBoxBottom",
    "继电器体积模型": "RelayVolumeModel",
    "电机外安装板": "MotorOuterMountingPlate",
    "减速箱": "Gearbox",
    "拨盘垫高板": "DialRaisingPlate",
    "上盖板": "UpperCoverPlate",
    "底板": "BasePlate",
    "机加工": "Machining",
    "销": "Pin",
    "步兵交叉滚子轴承座": "InfantryCrossedRollerBearingSeat",
    "上底": "UpperBase",
    "导电滑环安装转接板": "ConductiveSlipRingMountingAdapterPlate",
    "腿侧上保护板新": "LegSideUpperGuardPlateNew",
    "裁判系统支撑架": "RefereeSystemSupportFrame",
    "件": "Part",
    "弹道": "Trajectory",
    "纵梁加强": "LongitudinalBeamReinforcement",
    "下保护板": "LowerGuardPlate",
    "摩擦轮固定": "FrictionWheelFixing",
    "螺栓": "Bolt",
    "前挂载板": "FrontMountingPlate",
    "大臂": "LargeArm",
    "打印": "PrintDDD",
    "裁判系统": "RefereeSystem",
    "反向法兰边导电滑环": "ReverseFlangeConductingSlipRing",
    "装甲板保护板": "ArmorGuardPlate",
}


# --------------------------
# 配置
# --------------------------
src_folder = "/mnt/f/0Research&Develop/001-Sentry-Algo/Rename/assets"
dry_run = False   # True = 只打印不更改；改为 False 以实际重命名
rename_dirs = True  # 是否重命名目录名（True 推荐）
rename_files = True # 是否重命名文件名

# 先按中文长度从长到短排序，避免短词覆盖长词
sorted_keys = sorted(mapping.keys(), key=len, reverse=True)

def replace_all_in_name(name: str) -> str:
    new = name
    for zh in sorted_keys:
        en = mapping[zh]
        if zh in new:
            new = new.replace(zh, en)
    return new

def unique_path(path: str) -> str:
    """
    若 path 已存在，则在 filename 后加 _1/_2... 返回可用路径
    """
    base, ext = os.path.splitext(path)
    counter = 1
    candidate = path
    while os.path.exists(candidate):
        candidate = f"{base}_{counter}{ext}"
        counter += 1
    return candidate

# 主流程：从底向上遍历，这样先处理文件，再处理目录（避免重命名目录导致 walk 出问题）
changes = []  # (old_full_path, new_full_path)
for root, dirs, files in os.walk(src_folder, topdown=False):
    # 处理文件
    if rename_files:
        for fname in files:
            old_full = os.path.join(root, fname)
            new_fname = replace_all_in_name(fname)
            if new_fname != fname:
                new_full = os.path.join(root, new_fname)
                # 防止目标已存在，做唯一化
                if os.path.exists(new_full):
                    new_full = unique_path(new_full)
                changes.append((old_full, new_full))

    # 处理目录名本身（不包含 root 的父级）
    if rename_dirs:
        for dname in dirs:
            old_full = os.path.join(root, dname)
            new_dname = replace_all_in_name(dname)
            if new_dname != dname:
                new_full = os.path.join(root, new_dname)
                if os.path.exists(new_full):
                    new_full = unique_path(new_full)
                changes.append((old_full, new_full))

# 打印预览 / 执行
if not changes:
    print("没有发现需要替换的文件名或目录名。")
else:
    print(f"找到 {len(changes)} 个待重命名项（old -> new）：")
    for old, new in changes:
        print(f"{old}  ->  {new}")

    if dry_run:
        print("\ndry_run=True，未执行实际重命名。确认无误后将 dry_run 改为 False 再运行。")
    else:
        # 执行重命名
        for old, new in changes:
            try:
                os.rename(old, new)
            except Exception as e:
                print(f"重命名失败: {old} -> {new}   错误: {e}")
        print("重命名完成。")
