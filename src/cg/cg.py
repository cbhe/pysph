from ctypes import *

STRING = c_char_p


CG_COMPILED_PROGRAM = 4106
CG_DOUBLE1x1 = 1150
CG_TEXUNIT8 = 2056
CG_PROGRAM_ENTRY = 4105
CG_UCHAR2 = 1189
CG_HALF4x1 = 1041
CG_FIXED3x2 = 1083
CG_USHORT1x3 = 1236
CG_INVALID_PROGRAM_HANDLE_ERROR = 17
CG_COLOR5 = 2762
CG_PROFILE_UNKNOWN = 6145
CG_CHAR3x4 = 1182
CG_INT1 = 1094
CG_IN = 4097
CG_PROFILE_GLSLF = 7008
CG_PARAMETERCLASS_UNKNOWN = 0
CG_UNKNOWN = 4096
CG_BINORMAL3 = 2888
CG_TEX1 = 2180
CG_LONG4x4 = 1291
CG_LONG3x2 = 1285
CG_SHORT2x2 = 1218
CG_CHAR3x3 = 1181
CG_PROGRAM_SOURCE = 4104
CG_UCHAR1x2 = 1193
CG_FOG11 = 2928
CG_BUFFER_USAGE_STREAM_COPY = 2
CG_PARAMETERCLASS_STRUCT = 4
CG_COLOR12 = 2769
CG_BLENDINDICES4 = 2697
CG_SAMPLE13 = 2962
CG_LONG1 = 1272
CG_BLENDWEIGHT14 = 3042
CG_HLSL_UNIFORM = 3559
CG_CONFLICTING_PARAMETER_TYPES_ERROR = 25
CG_PROFILE_ARBFP1 = 7000
CG_FIXED1x2 = 1075
CG_SAMPLER3D = 1067
CG_TEXCOORD6 = 3226
CG_STRUCT = 1
CG_CHAR2x4 = 1178
CG_ULONG4x4 = 1312
CG_BOOL2x4 = 1126
CG_USHORT1x2 = 1235
CG_UCHAR2x3 = 1198
CG_FLOAT2 = 1046
CG_PROFILE_GP5VP = 7018
CG_INT = 1093
CG_INT4x1 = 1110
CG_CHAR1x4 = 1174
CG_LONG3x1 = 1284
CG_PARAMETER_IS_NOT_SHARED_ERROR = 26
CG_SHORT2x1 = 1217
CG_INVALID_SIZE_ERROR = 34
CG_ARRAY_PARAM_ERROR = 22
CG_FOG10 = 2927
CG_LITERAL = 4118
CG_BUFFER_USAGE_STATIC_COPY = 5
CG_ATTR3 = 2116
CG_ULONG3x2 = 1306
CG_BLENDWEIGHT13 = 3041
CG_PSIZE14 = 2835
CG_PROFILE_GS_4_0 = 6169
CG_UCHAR1x4 = 1195
CG_SAMPLE3 = 2952
CG_PROFILE_HS_5_0 = 6173
CG_BEHAVIOR_LATEST = 1
CG_PARAMETER_IS_NOT_RESIZABLE_ARRAY_ERROR = 33
CG_HALF1x4 = 1032
CG_SAMPLER2DSHADOW = 1314
CG_TANGENT0 = 2565
CG_COMBINER_CONST1 = 3285
CG_BLENDWEIGHT4 = 3032
CG_OFFSET_TEXTURE_MATRIX = 3288
CG_DOUBLE4x1 = 1162
CG_HALF1x3 = 1031
CG_CLP1 = 2311
CG_INVALID_POINTER_ERROR = 50
CG_USHORT1x1 = 1234
CG_PSIZE5 = 2826
CG_CLP0 = 2310
CG_POSITION3 = 2440
CG_PSIZ = 2309
CG_COL3 = 2248
CG_COL2 = 2247
CG_HALF4x4 = 1044
CG_COL1 = 2246
CG_COL0 = 2245
CG_NORMAL15 = 3107
CG_UINT1 = 1251
CG_HPOS = 2243
CG_LONG2x4 = 1283
CG_TEX7 = 2196
CG_TEX6 = 2195
CG_TANGENT3 = 2568
CG_COMBINER_STAGE_CONST0 = 3286
CG_TEX5 = 2194
CG_INVALID_PARAMETER_TYPE_ERROR = 32
CG_HALF1x1 = 1029
CG_TEX3 = 2192
CG_FOG9 = 2926
CG_INVALID_TECHNIQUE_ERROR = 49
CG_BEHAVIOR_CURRENT = 2000
CG_TEX2 = 2181
CG_DEPTH10 = 2943
CG_UINT4x2 = 1268
CG_TEX0 = 2179
CG_SAMPLE11 = 2960
CG_C = 2178
CG_BLENDWEIGHT12 = 3040
CG_ATTR15 = 2128
CG_PSIZE13 = 2834
CG_ATTR14 = 2127
CG_BINORMAL14 = 2899
CG_POSITION0 = 2437
CG_ATTR12 = 2125
CG_ATTR11 = 2124
CG_CHAR3 = 1169
CG_FOG7 = 2924
CG_ATTR10 = 2123
CG_TEXUNIT14 = 2062
CG_ATTR9 = 2122
CG_ATTR8 = 2121
CG_SHORT1 = 1209
CG_ATTR7 = 2120
CG_POINTCOORD = 2374
CG_ATTR6 = 2119
CG_INVALID_PASS_HANDLE_ERROR = 43
CG_TEXUNIT5 = 2053
CG_LASTCOL1 = 4401
CG_PROFILE_GENERIC = 7002
CG_UNDEFINED = 3256
CG_PROFILE_DS_5_0 = 6174
CG_HALF2 = 1026
CG_ATTR2 = 2115
CG_TEXUNIT31 = 4639
CG_PROFILE_GS_5_0 = 6172
CG_PROFILE_PS_5_0 = 6171
CG_POSITION8 = 2445
CG_BUFFER11 = 2075
CG_FLOAT1x1 = 1049
CG_BUFFER10 = 2074
CG_PSIZE15 = 2836
CG_PROFILE_PS_4_0 = 6168
CG_PROFILE_VS_5_0 = 6170
CG_PROFILE_VS_4_0 = 6167
CG_BUFFER7 = 2071
CG_BUFFER6 = 2070
CG_BUFFER5 = 2069
CG_TEXCOORD13 = 3233
CG_PROFILE_VS_3_0 = 6157
CG_BUFFER3 = 2067
CG_UINT2x3 = 1261
CG_HALF = 1025
CG_FOG0 = 2917
CG_BUFFER2 = 2066
CG_BLENDINDICES0 = 2693
CG_BUFFER1 = 2065
CG_CLP4 = 2314
CG_PROFILE_PS_1_3 = 6161
CG_PROFILE_PS_1_2 = 6160
CG_COLUMN_MAJOR = 4121
CG_BOOL4x4 = 1134
CG_TEXUNIT24 = 4632
CG_PROFILE_PS_1_1 = 6159
CG_ULONG2x4 = 1304
CG_BLENDWEIGHT11 = 3039
CG_TEXUNIT29 = 4637
CG_PSIZE12 = 2833
CG_PROFILE_VS_2_X = 6155
CG_TEXUNIT27 = 4635
CG_TEXCOORD12 = 3232
CG_CLP3 = 2313
CG_PROFILE_VS_1_1 = 6153
CG_TEXUNIT25 = 4633
CG_INVALID_ENUMERANT_ERROR = 10
CG_PROFILE_GP5TCP = 7020
CG_PROFILE_GP5GP = 7019
CG_TEXUNIT22 = 4630
CG_TEXUNIT21 = 4629
CG_TEXCOORD15 = 3235
CG_TEXUNIT20 = 4628
CG_TEXUNIT4 = 2052
CG_PROFILE_GP4VP = 7011
CG_TEXUNIT18 = 4626
CG_INNERTESS = 4419
CG_TEXUNIT17 = 4625
CG_TEXUNIT16 = 4624
CG_PROFILE_GPU_FP = 7010
CG_PSIZE8 = 2829
CG_PROFILE_GLSLC = 7009
CG_COLOR1 = 2758
CG_TEXCOORD9 = 3229
CG_COLOR6 = 2763
CG_ULONG3x4 = 1308
CG_FOG5 = 2922
CG_CHAR4 = 1170
CG_COLOR4 = 2761
CG_COLOR3 = 2760
CG_LONG2x2 = 1281
CG_NORMAL5 = 3097
CG_COLOR2 = 2759
CG_SHORT1x2 = 1214
CG_USHORT4 = 1233
CG_TEXCOORD8 = 3228
CG_FOG14 = 2931
CG_ULONG2x2 = 1302
CG_COMPILE_MANUAL = 4114
CG_STATE_ASSIGNMENT_TYPE_MISMATCH_ERROR = 47
CG_ULONG1x4 = 1300
CG_FILE_READ_ERROR = 12
CG_TEXUNIT12 = 2060
CG_DEPTH8 = 2941
CG_BLENDINDICES12 = 2705
CG_COLOR8 = 2765
CG_SAMPLE9 = 2958
CG_BOOL3x3 = 1129
CG_LINE = 4125
CG_ULONG2x3 = 1303
CG_ULONG4 = 1296
CG_PROFILE_HLSLF = 6166
CG_NOT_ROOT_PARAMETER_ERROR = 29
CG_BLENDINDICES5 = 2698
CG_UINT4x4 = 1270
CG_LASTCOL3 = 4403
CG_BLENDINDICES2 = 2695
CG_PROFILE_GP5FP = 7017
CG_PROFILE_FP40 = 6151
CG_BLENDINDICES1 = 2694
CG_CHAR1 = 1167
CG_UINT3x4 = 1266
CG_SAMPLER_RES = 3561
CG_TEXUNIT30 = 4638
CG_EDGETESS = 4418
CG_UINT3x1 = 1263
CG_UINT2x4 = 1262
CG_USHORT2 = 1231
CG_SPECULAR0 = 2629
CG_FOG2 = 2919
CG_TANGENT11 = 2576
CG_COLOR0 = 2757
CG_TANGENT10 = 2575
CG_TANGENT9 = 2574
CG_BUFFER8 = 2072
CG_UINT1x2 = 1256
CG_TANGENT6 = 2571
CG_LONG2x1 = 1280
CG_TANGENT5 = 2570
CG_PROGRAM_PROFILE = 4107
CG_SHORT1x1 = 1213
CG_INVALID_PARAMETER_ERROR = 2
CG_TANGENT2 = 2567
CG_IS_DIRECT3D_10_PROFILE = 4142
CG_TANGENT1 = 2566
CG_UCHAR1 = 1188
CG_INVALID_PARAMETER_HANDLE_ERROR = 46
CG_UCHAR4x4 = 1207
CG_UINT3x2 = 1264
CG_TEXUNIT7 = 2055
CG_UCHAR4x2 = 1205
CG_DIFFUSE0 = 2501
CG_COLOR7 = 2764
CG_POSITION15 = 2452
CG_SAMPLE8 = 2957
CG_TEXCOORD2 = 3222
CG_POINT = 4124
CG_POSITION14 = 2451
CG_UINT4x3 = 1269
CG_BLENDWEIGHT9 = 3037
CG_UCHAR3x4 = 1203
CG_IS_DIRECT3D_9_PROFILE = 4141
CG_BUFFER_USAGE_DYNAMIC_READ = 7
CG_POSITION12 = 2449
CG_ENV = 3302
CG_POSITION10 = 2447
CG_POSITION9 = 2446
CG_UCHAR2x2 = 1197
CG_BEHAVIOR_UNKNOWN = 0
CG_BUFFER_USAGE_DYNAMIC_DRAW = 6
CG_POSITION6 = 2443
CG_FIXED1x1 = 1074
CG_SAMPLER1DARRAY = 1138
CG_ULONG1 = 1293
CG_POSITION5 = 2442
CG_UCHAR1x3 = 1194
CG_HLSL_VARYING = 3560
CG_BOOL1x4 = 1122
CG_CONTROLPOINTID = 4417
CG_UCHAR4 = 1191
CG_UCHAR3 = 1190
CG_USHORT1 = 1230
CG_TANGENT15 = 2580
CG_ULONG = 1292
CG_WPOS = 2373
CG_BLENDINDICES15 = 2708
CG_CLP5 = 2315
CG_USHORT4x4 = 1249
CG_SHORT4x4 = 1228
CG_PROFILE_GLSLG = 7016
CG_BUFFER_USAGE_STATIC_READ = 4
CG_CLP2 = 2312
CG_ATTR0 = 2113
CG_LONG1x4 = 1279
CG_SHORT1x3 = 1215
CG_TEXUNIT13 = 2061
CG_USHORT3x4 = 1245
CG_SHORT4 = 1212
CG_SHORT3x4 = 1224
CG_FLOAT4x2 = 1062
CG_BOOL1x2 = 1120
CG_SHORT3x3 = 1223
CG_NORMAL10 = 3102
CG_FLOAT1x2 = 1050
CG_TEXUNIT9 = 2057
CG_UCHAR = 1187
CG_INVALID_TECHNIQUE_HANDLE_ERROR = 45
CG_SHORT2x4 = 1220
CG_BLENDWEIGHT10 = 3038
CG_DEPTH6 = 2939
CG_BOOL3x2 = 1128
CG_TEXUNIT6 = 2054
CG_MEMORY_ALLOC_ERROR = 15
CG_BOOL2 = 1116
CG_BLENDWEIGHT8 = 3036
CG_SHORT1x4 = 1216
CG_PROFILE_PS_3_0 = 6165
CG_TEXUNIT3 = 2051
CG_BUFFER_INDEX_OUT_OF_RANGE_ERROR = 58
CG_TEXUNIT2 = 2050
CG_BLENDINDICES13 = 2706
CG_TEXUNIT1 = 2049
CG_TEXUNIT0 = 2048
CG_NORMAL13 = 3105
CG_SHORT3 = 1211
CG_SHORT2 = 1210
CG_NORMAL12 = 3104
CG_SHORT = 1208
CG_PROFILE_GP4GP = 7012
CG_LONG4x2 = 1289
CG_FLOAT4 = 1048
CG_SAMPLEMASK = 4416
CG_BUFFER_USAGE_STREAM_DRAW = 0
CG_LONG3x4 = 1287
CG_TANGENT14 = 2579
CG_NORMAL11 = 3103
CG_LONG2x3 = 1282
CG_NORMAL14 = 3106
CG_BINORMAL7 = 2892
CG_INT1x1 = 1098
CG_BOOL1 = 1115
CG_PSIZE11 = 2832
CG_LONG1x2 = 1277
CG_HALF1x2 = 1030
CG_INVALID_PARAMETER_VARIABILITY_ERROR = 27
CG_TESSELLATION_CONTROL_DOMAIN = 4
CG_LONG3 = 1274
CG_TEXCOORD14 = 3234
CG_LONG2 = 1273
CG_BOOL = 1114
CG_LONG = 1271
CG_POSITION4 = 2441
CG_INT4x3 = 1112
CG_ATTR1 = 2114
CG_UCHAR4x3 = 1206
CG_INT3x4 = 1109
CG_NORMAL8 = 3100
CG_INT3x3 = 1108
CG_INT2x1 = 1102
CG_FRAGMENT_DOMAIN = 2
CG_INT3x1 = 1106
CG_INT2x4 = 1105
CG_BLENDWEIGHT3 = 3031
CG_BOOL4x3 = 1133
CG_INT2x2 = 1103
CG_USHORT2x3 = 1240
CG_PROFILE_GP5TEP = 7021
CG_DOUBLE2x3 = 1156
CG_VERTEX_DOMAIN = 1
CG_INVALID_CONTEXT_HANDLE_ERROR = 16
CG_INT1x3 = 1100
CG_INT1x2 = 1099
CG_LONG4x3 = 1290
CG_NO_ERROR = 0
CG_PROFILE_GLSLV = 7007
CG_INT2 = 1095
CG_BLENDWEIGHT1 = 3029
CG_CHAR2x2 = 1176
CG_HALF4x3 = 1043
CG_HALF4x2 = 1042
CG_LONG4x1 = 1288
CG_GEOMETRY_DOMAIN = 3
CG_FIXED4x1 = 1086
CG_SHORT4x3 = 1227
CG_PROFILE_VS_2_0 = 6154
CG_HALF3x4 = 1040
CG_BLENDWEIGHT0 = 3028
CG_UCHAR3x3 = 1202
CG_HALF3x3 = 1039
CG_TANGENT4 = 2569
CG_ROW_MAJOR = 4120
CG_USHORT2x1 = 1238
CG_HALF3x1 = 1037
CG_PROFILE_GP4FP = 7010
CG_ULONG1x3 = 1299
CG_PSIZE7 = 2828
CG_PARAMETERCLASS_OBJECT = 7
CG_PROFILE_ARBVP1 = 6150
CG_PROFILE_FP30 = 6149
CG_SAMPLE15 = 2964
CG_PROFILE_VP30 = 6148
CG_PROFILE_FP20 = 6147
CG_MAP_WRITE = 1
CG_PROFILE_VP20 = 6146
CG_UNCHANGED_CASE_POLICY = 4137
CG_BEHAVIOR_3000 = 2000
CG_TYPE_START_ENUM = 1024
CG_HALF4 = 1028
CG_LONG3x3 = 1286
CG_BOOL4x2 = 1132
CG_HALF3 = 1027
CG_GLSL_ATTRIB = 3301
CG_TEXUNIT23 = 4631
CG_HALF1 = 1090
CG_BOOL1x3 = 1121
CG_ULONG4x3 = 1311
CG_FLOAT4x3 = 1063
CG_IS_GEOMETRY_PROFILE = 4145
CG_PROFILE_PS_2_SW = 6164
CG_FLOAT4x1 = 1061
CG_FLOAT3x4 = 1060
CG_TEXUNIT19 = 4627
CG_HALF3x2 = 1038
CG_FLOAT3x3 = 1059
CG_BUFFER4 = 2068
CG_IS_OPENGL_PROFILE = 4138
CG_FLOAT3x1 = 1057
CG_SAMPLE12 = 2961
CG_FLOAT2x3 = 1055
CG_ULONG3x1 = 1305
CG_INVALID_VALUE_TYPE_ERROR = 8
CG_FLOAT2x2 = 1054
CG_FLOAT2x1 = 1053
CG_PARAMETERCLASS_MATRIX = 3
CG_FLOAT1x4 = 1052
CG_SHORT4x2 = 1226
CG_ATTR13 = 2126
CG_INVALID_STATE_ASSIGNMENT_HANDLE_ERROR = 42
CG_FLOAT1x3 = 1051
CG_NOT_4x4_MATRIX_ERROR = 11
CG_UCHAR3x2 = 1201
CG_BUFFER_USAGE_STATIC_DRAW = 3
CG_LONG4 = 1275
CG_TEXUNIT26 = 4634
CG_BUFFER_USAGE_STREAM_READ = 1
CG_PROFILE_GPU_GP = 7012
CG_ULONG1x2 = 1298
CG_FLOAT3 = 1047
CG_FIXED2x3 = 1080
CG_PROFILE_PS_2_X = 6163
CG_TESSELLATION_EVALUATION_DOMAIN = 5
CG_FLOAT1 = 1091
CG_FLOAT = 1045
CG_CANNOT_DESTROY_PARAMETER_ERROR = 28
CG_FIXED4x4 = 1089
CG_USHORT3 = 1232
CG_FIXED4x3 = 1088
CG_FIXED4x2 = 1087
CG_BUFFER9 = 2073
CG_FIXED2x2 = 1079
CG_NORMAL9 = 3101
CG_VERTEXSHADER_TYPE = 1141
CG_FIXED3x4 = 1085
CG_PSIZE10 = 2831
CG_BOOL4x1 = 1131
CG_PARAMETERCLASS_SAMPLER = 6
CG_IS_HLSL_PROFILE = 4147
CG_USHORT4x1 = 1246
CG_PARAMETERCLASS_ARRAY = 5
CG_CHAR3x1 = 1179
CG_DEPTH4 = 2937
CG_FIXED3x1 = 1082
CG_SAMPLEID = 4413
CG_FIXED2x4 = 1081
CG_POSITION2 = 2439
CG_POSITION11 = 2448
CG_PARAMETERCLASS_VECTOR = 2
CG_ULONG4x2 = 1310
CG_PARAMETERCLASS_SCALAR = 1
CG_PSIZE9 = 2830
CG_FIXED2x1 = 1078
CG_BLENDINDICES11 = 2704
CG_BLENDINDICES14 = 2707
CG_GLSLG_UNCOMBINED_LOAD_ERROR = 61
CG_BUFFER_UPDATE_NOT_ALLOWED_ERROR = 60
CG_FIXED1x4 = 1077
CG_UCHAR4x1 = 1204
CG_INT1x4 = 1101
CG_BINORMAL1 = 2886
CG_NORMAL6 = 3098
CG_FIXED4 = 1073
CG_FIXED3 = 1072
CG_USHORT2x4 = 1241
CG_UCHAR1x1 = 1192
CG_USHORT = 1229
CG_UNSUPPORTED_GL_EXTENSION_ERROR = 7
CG_SHORT4x1 = 1225
CG_CANNOT_SET_NON_UNIFORM_PARAMETER_ERROR = 54
CG_FIXED1x3 = 1076
CG_DOUBLE4x4 = 1165
CG_INVALID_STATE_HANDLE_ERROR = 41
CG_DOUBLE4x3 = 1164
CG_UCHAR3x1 = 1200
CG_NOT_ENOUGH_DATA_ERROR = 51
CG_CONSTANT = 4103
CG_UINT2x1 = 1259
CG_PROFILE_GPU_VP = 7011
CG_ULONG1x1 = 1297
CG_PROFILE_PS_2_0 = 6162
CG_DOUBLE3x3 = 1160
CG_PSIZE6 = 2827
CG_DOUBLE3x1 = 1158
CG_ULONG2x1 = 1301
CG_LAYER = 4415
CG_VERTEXID = 4414
CG_BUFFER_ALREADY_MAPPED_ERROR = 59
CG_SAMPLERRECTSHADOW = 1315
CG_PROGRAM_TYPE = 1136
CG_INSTANCEID = 4412
CG_LONG1x1 = 1276
CG_BOOL3x4 = 1130
CG_DOUBLE1x3 = 1152
CG_TYPE_IS_NOT_DEFINED_IN_PROGRAM_ERROR = 39
CG_TESSFACTOR = 3255
CG_LASTCOL6 = 4406
CG_DOUBLE3 = 1148
CG_BOOL2x2 = 1124
CG_ULONG4x1 = 1309
CG_LASTCOL4 = 4404
CG_THREAD_SAFE_POLICY = 4135
CG_BLENDINDICES10 = 2703
CG_LASTCOL2 = 4402
CG_PIXELSHADER_TYPE = 1142
CG_CHAR4x4 = 1186
CG_POINT_OUT = 4129
CG_HALF2x4 = 1036
CG_LASTCOL0 = 4400
CG_SAMPLE5 = 2954
CG_INVALID_BUFFER_HANDLE_ERROR = 57
CG_CHAR4x1 = 1183
CG_CHAR1x2 = 1172
CG_BLENDINDICES8 = 2701
CG_PROGRAM_NOT_LOADED_ERROR = 6
CG_CHAR3x2 = 1180
CG_OUT_OF_ARRAY_BOUNDS_ERROR = 23
CG_FIXED2 = 1071
CG_CONFLICTING_TYPES_ERROR = 24
CG_DOUBLE1x2 = 1151
CG_INVALID_EFFECT_HANDLE_ERROR = 40
CG_CHAR2x3 = 1177
CG_COMPILE_LAZY = 4116
CG_UCHAR2x4 = 1199
CG_DEPTH1 = 2934
CG_INVALID_OBJ_HANDLE_ERROR = 56
CG_UNIFORM = 4102
CG_OFFSET_TEXTURE_BIAS = 3290
CG_UINT1x4 = 1258
CG_SAMPLE2 = 2951
CG_ULONG2 = 1294
CG_CHAR1x3 = 1173
CG_DUPLICATE_NAME_ERROR = 55
CG_COMBINER_STAGE_CONST1 = 3287
CG_IS_DIRECT3D_11_PROFILE = 4153
CG_SAMPLE0 = 2949
CG_COMBINER_CONST0 = 3284
CG_BLENDINDICES6 = 2699
CG_NVPARSE_ERROR = 14
CG_FIXED = 1070
CG_CHAR = 1166
CG_SAMPLERRECT = 1068
CG_TRIANGLE_OUT = 4131
CG_TEXCOORD11 = 3231
CG_PROFILE_VP40 = 7001
CG_NOT_MATRIX_PARAM_ERROR = 9
CG_BLENDWEIGHT2 = 3030
CG_ARRAY_SIZE_MISMATCH_ERROR = 53
CG_TEXCOORD7 = 3227
CG_PROGRAM_BIND_ERROR = 5
CG_DEPTH14 = 2947
CG_BLENDINDICES9 = 2702
CG_TEXCOORD3 = 3223
CG_HALF2x3 = 1035
CG_COMPILER_ERROR = 1
CG_TEXCOORD1 = 3221
CG_TEXCOORD0 = 3220
CG_FOGCOORD = 3156
CG_USHORT2x2 = 1239
CG_USHORT4x3 = 1248
CG_BLENDINDICES3 = 2696
CG_BOOL1x1 = 1119
CG_BOOL4 = 1118
CG_DOUBLE4x2 = 1163
CG_BOOL3 = 1117
CG_USHORT3x3 = 1244
CG_TRIANGLE_ADJ = 4128
CG_USHORT3x2 = 1243
CG_VARYING = 4101
CG_USHORT3x1 = 1242
CG_UINT1x3 = 1257
CG_FIRST_DOMAIN = 1
CG_ULONG3 = 1295
CG_NORMAL7 = 3099
CG_SAMPLERCUBEARRAY = 1140
CG_UINT2 = 1252
CG_NORMAL3 = 3095
CG_DOUBLE2x4 = 1157
CG_PATCH = 4152
CG_TRIANGLE = 4127
CG_SAMPLERCUBE = 1069
CG_UCHAR2x1 = 1196
CG_UINT4x1 = 1267
CG_SAMPLER2DARRAY = 1139
CG_INT4 = 1097
CG_TEXTURE = 1137
CG_SAMPLER2D = 1066
CG_TEXCOORD10 = 3230
CG_PROFILE_HLSLV = 6158
CG_SAMPLER1DSHADOW = 1313
CG_UINT3x3 = 1265
CG_CONST_EYE = 3291
CG_SAMPLER1D = 1065
CG_FACE = 4410
CG_SAMPLER = 1143
CG_DOUBLE3x4 = 1161
CG_FIXED1 = 1092
CG_TANGENT8 = 2573
CG_FLOAT3x2 = 1058
CG_TEXUNIT15 = 2063
CG_HALF2x2 = 1034
CG_INVALID_FUNCTION_HANDLE_ERROR = 48
CG_BUFFER0 = 2064
CG_STRING = 1135
CG_ATTR5 = 2118
CG_ARRAY = 2
CG_PROGRAM_LOAD_ERROR = 4
CG_SHORT3x2 = 1222
CG_INVALID_DIMENSION_ERROR = 21
CG_DOUBLE3x2 = 1159
CG_BEHAVIOR_2200 = 1000
CG_DEPTH7 = 2940
CG_INT4x2 = 1111
CG_DEPTH3 = 2936
CG_MIXED = 4100
CG_VERSION = 4119
CG_UNKNOWN_DOMAIN = 0
CG_DEFERRED_PARAMETER_SETTING = 4133
CG_TANGENT13 = 2578
CG_SAMPLE4 = 2953
CG_FORCE_UPPER_CASE_POLICY = 4136
CG_TYPELESS_STRUCT = 3
CG_INT2x3 = 1104
CG_TEXCOORD5 = 3225
CG_CHAR2x1 = 1175
CG_TANGENT12 = 2577
CG_TEXUNIT11 = 2059
CG_LASTCOL7 = 4407
CG_BLENDWEIGHT5 = 3033
CG_INVALID_ANNOTATION_HANDLE_ERROR = 44
CG_POSITION7 = 2444
CG_ULONG3x3 = 1307
CG_MAP_WRITE_DISCARD = 3
CG_LONG1x3 = 1278
CG_BLENDINDICES7 = 2700
CG_MAP_READ_WRITE = 2
CG_UINT2x2 = 1260
CG_HALF2x1 = 1033
CG_MAP_READ = 0
CG_DOUBLE2x2 = 1155
CG_CHAR2 = 1168
CG_ATTR4 = 2117
CG_TEX4 = 2193
CG_TANGENT7 = 2572
CG_INVALID_PROFILE_ERROR = 3
CG_FLOAT4x4 = 1064
CG_SHORT3x1 = 1221
CG_VAR_ARG_ERROR = 20
CG_DOUBLE2x1 = 1154
CG_BOOL3x1 = 1127
CG_CHAR4x3 = 1185
CG_DEPTH2 = 2935
CG_INOUT = 4099
CG_UINT1x1 = 1255
CG_COLOR15 = 2772
CG_DOUBLE1x4 = 1153
CG_PROFILE_VS_2_SW = 6156
CG_NORMAL1 = 3093
CG_PSIZE1 = 2822
CG_FOG3 = 2920
CG_FILE_WRITE_ERROR = 13
CG_PRIMITIVEID = 4411
CG_FOG6 = 2923
CG_NORMAL4 = 3096
CG_DEPTH0 = 2933
CG_TEXCOORD4 = 3224
CG_FOG4 = 2921
CG_IS_TRANSLATION_PROFILE = 4146
CG_NORMAL2 = 3094
CG_OFFSET_TEXTURE_SCALE = 3289
CG_TEXUNIT10 = 2058
CG_DOUBLE4 = 1149
CG_FOG1 = 2918
CG_POSITION1 = 2438
CG_BLENDWEIGHT15 = 3043
CG_BINORMAL15 = 2900
CG_BINORMAL13 = 2898
CG_FLOAT2x4 = 1056
CG_BINORMAL12 = 2897
CG_BINORMAL11 = 2896
CG_ARRAY_HAS_WRONG_DIMENSION_ERROR = 38
CG_BINORMAL10 = 2895
CG_INT3 = 1096
CG_BINORMAL9 = 2894
CG_INT4x4 = 1113
CG_BLENDWEIGHT7 = 3035
CG_BLENDWEIGHT6 = 3034
CG_UINT4 = 1254
CG_COVERAGE = 3292
CG_BINORMAL6 = 2891
CG_BINORMAL5 = 2890
CG_UNKNOWN_PROFILE_ERROR = 19
CG_ARRAY_DIMENSIONS_DO_NOT_MATCH_ERROR = 37
CG_POSITION13 = 2450
CG_BINORMAL4 = 2889
CG_BINORMAL8 = 2893
CG_IS_TESSELLATION_EVALUATION_PROFILE = 4150
CG_FOG13 = 2930
CG_BINORMAL2 = 2887
CG_NON_NUMERIC_PARAMETER_ERROR = 52
CG_OUT = 4098
CG_IS_GLSL_PROFILE = 4148
CG_UINT3 = 1253
CG_TEXUNIT28 = 4636
CG_BINORMAL0 = 2885
CG_SAMPLE14 = 2963
CG_BUFFER_USAGE_DYNAMIC_COPY = 8
CG_ARRAY_TYPES_DO_NOT_MATCH_ERROR = 36
CG_NORMAL0 = 3092
CG_IS_FRAGMENT_PROFILE = 4144
CG_FOG12 = 2929
CG_IS_VERTEX_PROFILE = 4143
CG_GLSL_UNIFORM = 3300
CG_SAMPLE10 = 2959
CG_SAMPLE7 = 2956
CG_IS_DIRECT3D_8_PROFILE = 4140
CG_IS_DIRECT3D_PROFILE = 4139
CG_SAMPLE6 = 2955
CG_ERROR = 4111
CG_BOOL2x3 = 1125
CG_UNKNOWN_TYPE = 0
CG_INT3x2 = 1107
CG_PSIZE4 = 2825
CG_LASTCOL5 = 4405
CG_NO_LOCKS_POLICY = 4134
CG_SAMPLE1 = 2950
CG_BOOL2x1 = 1123
CG_IMMEDIATE_PARAMETER_SETTING = 4132
CG_COLOR10 = 2767
CG_FIXED3x3 = 1084
CG_DEPTH15 = 2948
CG_USHORT1x4 = 1237
CG_LINE_OUT = 4130
CG_UINT = 1250
CG_DEPTH13 = 2946
CG_DEPTH12 = 2945
CG_DOUBLE = 1145
CG_DEPTH11 = 2944
CG_LINE_ADJ = 4126
CG_COLOR9 = 2766
CG_CHAR1x1 = 1171
CG_DEPTH9 = 2942
CG_GLOBAL = 4108
CG_VERTEX = 4123
CG_SHORT2x3 = 1219
CG_USHORT4x2 = 1247
CG_FRAGMENT = 4122
CG_INVALID_PARAM_HANDLE_ERROR = 18
CG_DEPTH5 = 2938
CG_FOG15 = 2932
CG_BIND_CREATES_CYCLE_ERROR = 35
CG_COMPILE_IMMEDIATE = 4115
CG_DOUBLE2 = 1147
CG_PSIZE2 = 2823
CG_DOUBLE1 = 1146
CG_CURRENT = 4117
CG_OBJECT = 4113
CG_PSIZE0 = 2821
CG_IS_NOT_PROGRAM_PARAMETER_ERROR = 31
CG_COLOR14 = 2771
CG_COLOR13 = 2770
CG_SOURCE = 4112
CG_MAP_WRITE_NO_OVERWRITE = 4
CG_COLOR11 = 2768
CG_PARAMETERS_DO_NOT_MATCH_ERROR = 30
CG_DEFAULT = 4110
CG_CHAR4x2 = 1184
CG_PROGRAM = 4109
CG_IS_TESSELLATION_CONTROL_PROFILE = 4149
CG_FOG8 = 2925
CG_SAMPLERBUF = 1144
CG_PSIZE3 = 2824
CG_VERSION_NUM = 3000 # Variable c_int '3000'
CG_FALSE = 0 # Variable c_int '0'
CG_TRUE = 1 # Variable c_int '1'
CGbool = c_int
class _CGcontext(Structure):
    pass
_CGcontext._fields_ = [
]
CGcontext = POINTER(_CGcontext)
class _CGprogram(Structure):
    pass
_CGprogram._fields_ = [
]
CGprogram = POINTER(_CGprogram)
class _CGparameter(Structure):
    pass
_CGparameter._fields_ = [
]
CGparameter = POINTER(_CGparameter)
class _CGobj(Structure):
    pass
_CGobj._fields_ = [
]
CGobj = POINTER(_CGobj)
class _CGbuffer(Structure):
    pass
CGbuffer = POINTER(_CGbuffer)
_CGbuffer._fields_ = [
]
class _CGeffect(Structure):
    pass
CGeffect = POINTER(_CGeffect)
_CGeffect._fields_ = [
]
class _CGtechnique(Structure):
    pass
CGtechnique = POINTER(_CGtechnique)
_CGtechnique._fields_ = [
]
class _CGpass(Structure):
    pass
_CGpass._fields_ = [
]
CGpass = POINTER(_CGpass)
class _CGstate(Structure):
    pass
_CGstate._fields_ = [
]
CGstate = POINTER(_CGstate)
class _CGstateassignment(Structure):
    pass
CGstateassignment = POINTER(_CGstateassignment)
_CGstateassignment._fields_ = [
]
class _CGannotation(Structure):
    pass
CGannotation = POINTER(_CGannotation)
_CGannotation._fields_ = [
]
CGhandle = c_void_p

# values for enumeration 'CGbehavior'
CGbehavior = c_int # enum

# values for enumeration 'CGtype'
CGtype = c_int # enum

# values for enumeration 'CGresource'
CGresource = c_int # enum

# values for enumeration 'CGprofile'
CGprofile = c_int # enum

# values for enumeration 'CGerror'
CGerror = c_int # enum

# values for enumeration 'CGenum'
CGenum = c_int # enum

# values for enumeration 'CGparameterclass'
CGparameterclass = c_int # enum

# values for enumeration 'CGdomain'
CGdomain = c_int # enum

# values for enumeration 'CGbufferaccess'
CGbufferaccess = c_int # enum

# values for enumeration 'CGbufferusage'
CGbufferusage = c_int # enum
CGstatecallback = CFUNCTYPE(CGbool, CGstateassignment)
CGerrorCallbackFunc = CFUNCTYPE(None)
CGerrorHandlerFunc = CFUNCTYPE(None, CGcontext, CGerror, c_void_p)
CGIncludeCallbackFunc = CFUNCTYPE(None, CGcontext, STRING)
__all__ = ['CGerrorHandlerFunc',
           'CG_IS_TESSELLATION_EVALUATION_PROFILE',
           'CG_PROFILE_GP4VP', 'CG_SOURCE', 'CG_SAMPLER_RES',
           'CG_FIRST_DOMAIN', 'CG_CONFLICTING_TYPES_ERROR',
           'CG_BLENDINDICES10', 'CG_VERTEXID',
           'CG_ARRAY_TYPES_DO_NOT_MATCH_ERROR', 'CG_UCHAR2x3',
           'CG_DEPTH10', 'CG_UCHAR2x1', 'CG_DEPTH12', 'CG_DEPTH15',
           'CG_DEPTH14', 'CG_UCHAR2x4', 'CG_LASTCOL4', 'CG_LASTCOL5',
           'CG_LASTCOL6', 'CG_PROFILE_GP5TEP', 'CG_LASTCOL0',
           'CG_LASTCOL1', 'CG_LASTCOL2', 'CG_LASTCOL3', 'CG_LONG2x1',
           'CG_INVALID_ENUMERANT_ERROR', 'CG_PROFILE_VP20',
           'CG_UNKNOWN_DOMAIN', 'CG_UCHAR', 'CG_USHORT2x3', 'CG_ENV',
           'CG_DIFFUSE0', 'CG_GLSL_ATTRIB', '_CGpass',
           'CG_SAMPLER2DARRAY', 'CG_DOUBLE4x2', 'CG_ULONG1x2',
           'CG_TESSFACTOR', 'CG_DOUBLE4x1', 'CG_DOUBLE4x4',
           'CG_FLOAT3', 'CG_TEXCOORD0', 'CG_INVALID_TECHNIQUE_ERROR',
           'CG_ULONG1x1', 'CG_INT',
           'CG_INVALID_STATE_ASSIGNMENT_HANDLE_ERROR',
           'CG_COMPILE_LAZY', 'CG_PROFILE_GPU_FP',
           'CG_IS_NOT_PROGRAM_PARAMETER_ERROR', 'CG_FLOAT4',
           'CGtechnique', 'CGprogram', 'CG_NVPARSE_ERROR',
           'CG_COMPILE_IMMEDIATE', 'CG_SAMPLEMASK',
           'CG_UNCHANGED_CASE_POLICY', 'CG_IS_OPENGL_PROFILE',
           'CG_FOG13', 'CG_BUFFER_UPDATE_NOT_ALLOWED_ERROR',
           'CG_VERTEX_DOMAIN', 'CG_GLSL_UNIFORM', 'CG_BLENDWEIGHT15',
           'CG_SHORT3x4', 'CG_SHORT3x3', 'CG_SHORT3x2', 'CG_SHORT3x1',
           'CG_COMPILER_ERROR', 'CG_OUT', 'CG_INT4x4', 'CG_INT4x1',
           'CG_INT4x3', 'CG_INT4x2', 'CG_HALF1x1', 'CG_HALF1x3',
           'CG_HALF1x2', 'CG_HALF1x4', 'CG_COMPILED_PROGRAM',
           'CG_OFFSET_TEXTURE_SCALE', 'CG_BINORMAL9',
           'CGparameterclass', 'CG_UCHAR4x4', 'CG_UCHAR4x1',
           'CG_SAMPLER2D', 'CG_UCHAR4x3', 'CG_UCHAR4x2',
           'CG_TANGENT8', 'CG_UINT1x4', 'CG_BUFFER9', 'CG_BUFFER8',
           'CG_BUFFER7', 'CG_BUFFER6', 'CG_CLP5', 'CG_CLP4',
           'CG_CLP3', 'CG_BUFFER2', 'CG_CLP1', 'CG_CLP0', 'CG_ULONG1',
           'CG_ULONG3', 'CG_ULONG2', 'CG_TEXUNIT28', 'CG_ULONG4',
           'CG_TEXUNIT24', 'CG_TEXUNIT25', 'CG_TEXUNIT26',
           'CG_TEXUNIT27', 'CG_TEXUNIT20', 'CG_TEXUNIT21',
           'CG_TEXUNIT22', 'CG_TEXUNIT23', 'CG_UINT4x1', 'CG_UINT4x3',
           'CG_UINT4x2', 'CG_UINT4x4',
           'CG_INVALID_ANNOTATION_HANDLE_ERROR', 'CG_SAMPLE10',
           'CG_DEPTH11', 'CG_INVALID_TECHNIQUE_HANDLE_ERROR',
           'CG_UCHAR2x2', 'CG_PROFILE_FP40', 'CG_DEPTH13',
           'CG_NO_LOCKS_POLICY', 'CG_LINE_OUT', 'CG_USHORT3x3',
           'CG_SAMPLER', 'CG_BUFFER_USAGE_STREAM_COPY', 'CG_PSIZE9',
           'CG_SAMPLER1DARRAY', 'CG_PSIZE5', 'CG_PSIZE4', 'CG_PSIZE7',
           'CG_PSIZE6', 'CG_PSIZE1', 'CG_PSIZE0', 'CG_PSIZE3',
           'CG_FOGCOORD', 'CG_PROFILE_HLSLV', 'CG_LASTCOL7',
           'CGeffect', 'CG_FORCE_UPPER_CASE_POLICY',
           'CG_PROFILE_HLSLF', 'CG_OFFSET_TEXTURE_MATRIX',
           'CG_INVALID_PARAMETER_ERROR', 'CG_UNKNOWN_PROFILE_ERROR',
           'CG_PROFILE_FP30', 'CG_LONG1x2', 'CG_LONG1x3',
           'CG_LONG1x1', 'CG_ERROR', 'CG_LONG1x4',
           'CGstateassignment', 'CG_COMBINER_CONST0',
           'CG_INVALID_BUFFER_HANDLE_ERROR',
           'CG_INVALID_POINTER_ERROR', 'CG_FILE_READ_ERROR',
           'CG_FLOAT2x2', 'CG_FLOAT2x3', 'CG_FLOAT2x1', 'CG_FLOAT2x4',
           'CG_TRIANGLE_OUT', 'CG_POINT_OUT', 'CG_SAMPLER1D',
           'CG_PRIMITIVEID', 'CG_BINORMAL5', 'CG_BINORMAL4',
           'CG_BINORMAL7', 'CG_BINORMAL6', 'CG_BINORMAL1',
           'CG_BINORMAL0', 'CG_BINORMAL3', 'CG_BINORMAL2',
           'CG_CONST_EYE', 'CG_BINORMAL8', 'CG_INT3x2', 'CG_INT3x3',
           'CG_OBJECT', 'CG_INT3x1', 'CG_INT3x4', 'CG_UINT4',
           'CG_EDGETESS', 'CG_SAMPLERRECTSHADOW', 'CG_BOOL1x2',
           'CGannotation', 'CG_COL0', 'CG_COL1', 'CG_COL2', 'CG_COL3',
           'CG_TANGENT3', 'CG_DOUBLE2', 'CG_DOUBLE3', 'CG_DOUBLE4',
           'CG_INVALID_CONTEXT_HANDLE_ERROR', '_CGobj', 'CGerror',
           'CGhandle', 'CG_USHORT2', 'CG_USHORT3', 'CG_USHORT1',
           'CG_LONG', 'CG_USHORT4', 'CG_PROFILE_GP5VP', 'CG_SAMPLE0',
           'CG_TANGENT12', 'CG_POINT', 'CG_PROFILE_ARBVP1',
           'CG_TRIANGLE_ADJ', 'CG_INVALID_OBJ_HANDLE_ERROR',
           'CG_INT2x3', 'CG_INVALID_PARAMETER_VARIABILITY_ERROR',
           'CG_INT2x1', 'CG_INT2x4', 'CG_HALF3x3', 'CG_HALF3x2',
           'CG_HALF3x1', 'CG_ULONG4x4', 'CG_ULONG4x3',
           'CG_IS_HLSL_PROFILE', 'CG_ULONG4x1', 'CG_HALF3x4',
           'CG_PROFILE_PS_5_0', 'CG_UINT',
           'CG_BUFFER_USAGE_DYNAMIC_COPY', 'CGprofile', 'CG_IN',
           '_CGeffect', 'CG_INVALID_PARAMETER_TYPE_ERROR',
           'CG_FRAGMENT', 'CG_HALF', 'CG_DOUBLE4x3', 'CG_DOUBLE1x4',
           'CG_DOUBLE1x3', 'CG_DOUBLE1x2', 'CG_DOUBLE1x1',
           'CG_GLSLG_UNCOMBINED_LOAD_ERROR', 'CG_FLOAT4x4',
           'CG_SHORT1x4', 'CG_SHORT1x1', 'CG_FLOAT4x1', 'CG_FLOAT4x2',
           'CG_SHORT1x2', 'CG_LINE', 'CG_CHAR4x3', 'CG_CHAR4x2',
           'CG_CHAR4x4', 'CG_COLOR14', 'CG_ULONG', 'CG_NORMAL2',
           'CG_TRUE', 'CG_NORMAL3', 'CG_TESSELLATION_CONTROL_DOMAIN',
           'CG_MAP_WRITE_DISCARD', 'CGresource', 'CG_BOOL4',
           'CG_COLOR7', 'CG_COLOR6', 'CG_COLOR5', 'CG_COLOR4',
           'CG_COLOR3', 'CG_COLOR2', 'CG_COLOR1', 'CG_COLOR0',
           'CG_BLENDINDICES0', 'CG_COLOR9', 'CG_COLOR8', 'CG_BOOL2x3',
           'CG_BOOL2x2', 'CG_BOOL2x1', 'CG_HPOS', 'CG_BOOL2x4',
           'CG_INVALID_DIMENSION_ERROR', 'CG_DEPTH1', 'CG_DEPTH0',
           'CG_DEPTH3', 'CG_LONG4x4', 'CG_LONG4x3', 'CG_LONG4x2',
           'CG_LONG4x1', 'CG_DEPTH6', 'CG_DEPTH9', 'CG_DEPTH8',
           'CG_NO_ERROR', 'CG_NORMAL8', 'CG_PROGRAM', 'CG_NORMAL9',
           'CG_IS_DIRECT3D_11_PROFILE', 'CG_FLOAT3x3',
           'CG_PROFILE_GP5TCP', 'CG_BLENDINDICES15',
           'CG_BLENDINDICES14', 'CG_BLENDINDICES13',
           'CG_BLENDINDICES12', 'CG_BLENDINDICES11', 'CG_FLOAT3x4',
           'CG_IS_FRAGMENT_PROFILE', 'CGbehavior',
           'CG_IS_DIRECT3D_8_PROFILE', 'CG_NOT_ROOT_PARAMETER_ERROR',
           'CG_PARAMETERS_DO_NOT_MATCH_ERROR', 'CG_FOG12',
           'CG_PROFILE_PS_3_0', 'CG_BEHAVIOR_3000', 'CG_MAP_READ',
           'CG_IS_GLSL_PROFILE', 'CG_UCHAR1x1', 'CG_UCHAR1x2',
           'CG_UCHAR1x3', 'CG_UCHAR1x4', 'CG_IS_TRANSLATION_PROFILE',
           'CG_FOG15', 'CG_PROFILE_PS_1_1', 'CG_PROFILE_PS_1_2',
           'CG_PROFILE_PS_1_3', 'CG_PROFILE_ARBFP1',
           'CG_BUFFER_USAGE_STREAM_READ', 'CG_VERTEXSHADER_TYPE',
           'CG_BIND_CREATES_CYCLE_ERROR', 'CG_LINE_ADJ',
           'CG_USHORT4x1', 'CG_PARAMETERCLASS_VECTOR', 'CG_USHORT4x2',
           'CG_DOUBLE', 'CG_PSIZE15', 'CG_PSIZE14', 'CG_USHORT4x3',
           'CG_PSIZE11', 'CG_PSIZE10', 'CG_PSIZE13', 'CG_PSIZE12',
           'CG_ULONG2x1', 'CG_INT1x4', 'CG_ULONG2x3', 'CG_ULONG2x2',
           'CG_ULONG2x4', 'CG_BINORMAL15', 'CG_BINORMAL14',
           'CG_BINORMAL11', 'CG_BINORMAL10', 'CG_BINORMAL13',
           'CG_BINORMAL12', 'CG_TYPE_START_ENUM', 'CG_INT1x1',
           'CG_INT1x2', 'CG_INT1x3', 'CG_USHORT4x4', 'CG_ULONG3x1',
           'CG_ULONG3x2', 'CG_ULONG3x3',
           'CG_BUFFER_USAGE_STATIC_READ', 'CG_ULONG3x4',
           'CG_COMBINER_STAGE_CONST1', 'CG_COMBINER_STAGE_CONST0',
           'CG_PROFILE_DS_5_0', 'CG_PROFILE_GPU_GP', 'CG_BOOL1x1',
           'CGparameter', 'CG_VERSION', 'CG_TEXUNIT31',
           'CG_TEXUNIT30', 'CG_FOG6', 'CG_FOG7', 'CG_FOG4', 'CG_FOG5',
           'CG_FOG2', 'CG_FOG3', 'CG_FOG0', 'CG_FOG1',
           'CG_MAP_READ_WRITE', 'CG_FOG8', 'CG_FOG9', 'CG_TEXTURE',
           'CG_SAMPLERCUBE', 'CG_PROFILE_FP20', 'CGerrorCallbackFunc',
           'CG_DOUBLE1', '_CGannotation', 'CG_CHAR4', 'CG_CHAR3',
           'CG_CHAR2', 'CG_CHAR1', 'CG_INVALID_PROFILE_ERROR',
           'CG_FIXED2x2', 'CG_FIXED2x3', 'CG_FIXED2x1',
           'CG_COMPILE_MANUAL', 'CG_FIXED2x4', 'CG_BOOL3x2',
           'CG_BOOL3x3', 'CG_NOT_4x4_MATRIX_ERROR', 'CG_SAMPLERRECT',
           'CG_GEOMETRY_DOMAIN', 'CGdomain', 'CG_COVERAGE',
           'CG_MAP_WRITE', 'CG_ULONG4x2', 'CG_INOUT',
           'CG_INVALID_PASS_HANDLE_ERROR', 'CG_PROFILE_PS_4_0',
           'CG_CURRENT', 'CG_DOUBLE3x1', 'CG_DOUBLE3x3',
           'CG_ROW_MAJOR', 'CG_NOT_MATRIX_PARAM_ERROR', 'CG_BOOL4x4',
           'CG_HLSL_UNIFORM', 'CG_BOOL4x1', 'CG_BOOL4x3',
           'CG_BOOL4x2', 'CG_TRIANGLE', 'CG_PROFILE_PS_2_0',
           'CG_PROGRAM_SOURCE', 'CG_MEMORY_ALLOC_ERROR', 'CG_UNKNOWN',
           'CG_INNERTESS', 'CG_PROGRAM_TYPE',
           'CG_OFFSET_TEXTURE_BIAS', 'CG_PROFILE_PS_2_X', 'CG_LAYER',
           'CGbufferusage', 'CG_NOT_ENOUGH_DATA_ERROR',
           'CG_PROFILE_GS_4_0',
           'CG_ARRAY_DIMENSIONS_DO_NOT_MATCH_ERROR', 'CG_WPOS',
           'CG_IS_GEOMETRY_PROFILE', 'CG_FLOAT', 'CG_PROFILE_VS_2_SW',
           'CG_SAMPLERBUF', 'CG_BEHAVIOR_2200', 'CG_UINT2x4',
           'CG_UINT2x3', 'CG_UINT2x2', 'CG_UINT2x1', 'CG_USHORT2x4',
           'CG_USHORT2x2', 'CG_IS_DIRECT3D_10_PROFILE',
           'CG_USHORT2x1', 'CG_FLOAT2', 'CG_ULONG1x3', 'CG_FLOAT1',
           'CG_ARRAY_PARAM_ERROR', 'CG_ULONG1x4',
           'CG_BUFFER_ALREADY_MAPPED_ERROR', 'CG_SHORT',
           'CG_TANGENT13', 'CG_TEXCOORD1', 'CG_TANGENT11',
           'CG_TANGENT10', 'CG_TANGENT15', 'CG_TANGENT14',
           'CG_UCHAR3x2', 'CG_UCHAR3x3', 'CG_SAMPLE15', 'CG_UCHAR3x1',
           'CG_SAMPLE13', 'CG_SAMPLE12', 'CG_SAMPLE11', 'CG_UINT1x3',
           'CG_USHORT3x4', 'CG_PROFILE_GP4FP', 'CG_USHORT3x2',
           'CG_USHORT3x1', '_CGtechnique', 'CG_FIXED4x1', '_CGbuffer',
           'CG_TEXCOORD7', 'CG_BUFFER_USAGE_DYNAMIC_DRAW',
           'CG_FIXED4x3', 'CG_SAMPLE7', 'CG_SAMPLE6', 'CG_SAMPLE5',
           'CG_SAMPLE4', 'CG_SAMPLE3', 'CG_SAMPLE2', 'CG_SAMPLE1',
           'CG_SHORT4x1', 'CG_INVALID_VALUE_TYPE_ERROR', 'CG_SAMPLE9',
           'CG_SAMPLE8', 'CG_BEHAVIOR_UNKNOWN', 'CG_PROFILE_GENERIC',
           'CG_HALF2', 'CG_HALF3', 'CG_HALF1', 'CG_PIXELSHADER_TYPE',
           'CG_HALF4', 'CG_BOOL1x3', 'CG_POSITION0', 'CG_POSITION1',
           'CG_POSITION2', 'CG_POSITION3', 'CG_POSITION4',
           'CG_POSITION5', 'CG_POSITION6', 'CG_POSITION7',
           'CG_POSITION8', 'CG_POSITION9',
           'CG_INVALID_EFFECT_HANDLE_ERROR', 'CG_FIXED3x3',
           'CG_FIXED3x2', 'CG_FIXED3x1', 'CG_FIXED3x4',
           'CG_PARAMETERCLASS_OBJECT', 'CG_C', 'CG_UNIFORM',
           'CG_PROFILE_VS_2_0', 'CG_PROFILE_VS_4_0', 'CG_CHAR',
           'CG_DEFERRED_PARAMETER_SETTING', 'CG_FIXED4x4',
           'CG_PROFILE_GPU_VP', 'CG_TEXCOORD3', 'CG_TEXCOORD2',
           'CG_TEXCOORD5',
           'CG_PARAMETER_IS_NOT_RESIZABLE_ARRAY_ERROR', 'CG_FIXED4x2',
           'CG_TEXCOORD6', 'CG_TEXCOORD9', 'CG_TEXCOORD8',
           'CG_SHORT4x2', 'CG_SHORT4x3', 'CG_SHORT4x4',
           'CG_SPECULAR0', '_CGparameter', 'CGstate',
           'CG_NON_NUMERIC_PARAMETER_ERROR', 'CG_INT2x2',
           'CG_TYPELESS_STRUCT', 'CG_CONSTANT', 'CG_PROFILE_GLSLV',
           '_CGcontext', 'CG_FACE',
           'CG_TYPE_IS_NOT_DEFINED_IN_PROGRAM_ERROR',
           'CG_PROFILE_GLSLC', 'CG_PROFILE_GLSLG', 'CG_PROFILE_GLSLF',
           'CG_UNSUPPORTED_GL_EXTENSION_ERROR',
           'CG_CANNOT_DESTROY_PARAMETER_ERROR', 'CG_LONG1',
           'CG_LONG3', 'CG_LONG2', 'CG_PROFILE_VS_2_X', 'CGtype',
           'CG_LONG3x1', 'CG_LONG3x2', 'CG_SAMPLER2DSHADOW',
           'CG_LONG3x4', '_CGstate', 'CG_PARAMETERCLASS_SAMPLER',
           'CG_TEXCOORD4', 'CG_COLOR13', 'CG_COLOR12', 'CG_COLOR11',
           'CG_COLOR10', 'CG_TEXCOORD11', 'CG_TEXCOORD10',
           'CG_TEXCOORD13', 'CG_TEXCOORD12', 'CG_UINT3x2',
           'CG_COMBINER_CONST1', 'CG_UINT3x1', 'CG_USHORT1x4',
           'CG_USHORT1x1', 'CG_USHORT1x3', 'CG_USHORT1x2',
           'CG_PROFILE_GS_5_0', 'CG_IS_DIRECT3D_PROFILE',
           'CG_SAMPLEID', 'CG_HALF2x1', 'CGbool', 'CG_BOOL',
           'CG_IS_TESSELLATION_CONTROL_PROFILE',
           'CG_PARAMETERCLASS_MATRIX',
           'CG_IMMEDIATE_PARAMETER_SETTING', 'CG_BLENDINDICES9',
           'CG_BLENDINDICES8', 'CG_HALF2x4', 'CG_BLENDINDICES3',
           'CG_BLENDINDICES2', 'CG_BLENDINDICES1', 'CG_CHAR2x4',
           'CG_CHAR2x3', 'CG_CHAR2x2', 'CG_BLENDINDICES5',
           'CG_BLENDINDICES4', 'CG_BUFFER_USAGE_STATIC_DRAW',
           'CG_BOOL3x4', 'CG_INVALID_PARAM_HANDLE_ERROR',
           'CG_CONFLICTING_PARAMETER_TYPES_ERROR',
           'CG_MAP_WRITE_NO_OVERWRITE', 'CG_USHORT', 'CG_INT4',
           'CG_INT3', 'CG_INT2', 'CG_INT1', 'CG_PROFILE_GP5GP',
           'CG_CHAR1x4', 'CG_PSIZE2', 'CG_CHAR1x1', 'CG_CHAR1x2',
           'CG_CHAR1x3', 'CG_VERSION_NUM', 'CG_INSTANCEID',
           'CG_HLSL_VARYING',
           'CG_CANNOT_SET_NON_UNIFORM_PARAMETER_ERROR',
           'CG_BUFFER_USAGE_STATIC_COPY', 'CG_UNDEFINED',
           '_CGstateassignment', 'CG_FLOAT1x1', 'CG_FLOAT1x3',
           'CG_FLOAT1x2', 'CG_FLOAT1x4', 'CG_PROGRAM_PROFILE',
           'CG_IS_DIRECT3D_9_PROFILE', 'CGobj', 'CG_UINT1x1',
           'CG_NORMAL10', 'CG_NORMAL11', 'CG_NORMAL12', 'CG_NORMAL13',
           'CG_NORMAL14', 'CG_NORMAL15', 'CG_LONG4',
           'CG_INVALID_SIZE_ERROR', 'CG_FOG10', 'CG_FOG11',
           'CG_INVALID_STATE_HANDLE_ERROR', 'CG_UINT1x2', 'CG_FOG14',
           'CG_LONG2x3', 'CGpass', 'CG_PROGRAM_LOAD_ERROR',
           'CG_BUFFER5', 'CGenum', 'CG_LONG3x3', 'CG_UINT3',
           'CG_UINT2', 'CG_UINT1', 'CG_BUFFER3', 'CG_BOOL3x1',
           'CG_CLP2', 'CG_SAMPLERCUBEARRAY', 'CG_BUFFER1',
           'CG_DOUBLE3x4', 'CG_BUFFER0', 'CG_SHORT1x3',
           'CG_VAR_ARG_ERROR', 'CG_FLOAT4x3', 'CG_COLOR15',
           'CG_PROFILE_VP30', 'CG_CHAR4x1', 'CG_PROFILE_VS_1_1',
           'CG_BUFFER_USAGE_STREAM_DRAW', 'CGcontext',
           'CG_FRAGMENT_DOMAIN', 'CGbuffer', 'CG_DOUBLE3x2',
           'CG_PARAMETERCLASS_SCALAR', 'CG_TEXUNIT29', 'CG_SAMPLER3D',
           'CG_PARAMETERCLASS_UNKNOWN', 'CG_MIXED',
           'CG_PROFILE_VS_5_0', 'CG_HALF2x2', 'CG_HALF2x3',
           'CG_STRUCT', 'CGbufferaccess', 'CG_PARAMETERCLASS_STRUCT',
           'CG_PROFILE_VP40', 'CG_UINT3x4', 'CG_ATTR0', 'CG_ATTR1',
           'CG_ATTR2', 'CG_ATTR3', 'CG_ATTR4', 'CG_ATTR5', 'CG_ATTR6',
           'CG_ATTR7', 'CG_ATTR8', 'CG_ATTR9', 'CG_TEXCOORD14',
           'CGIncludeCallbackFunc', 'CG_CHAR3x4', 'CG_CHAR3x2',
           'CG_CHAR3x3', 'CG_CHAR3x1', 'CG_UNKNOWN_TYPE',
           'CG_BUFFER_INDEX_OUT_OF_RANGE_ERROR', 'CG_PROFILE_VS_3_0',
           'CG_UCHAR3', 'CG_UCHAR2',
           'CG_PARAMETER_IS_NOT_SHARED_ERROR',
           'CG_ARRAY_HAS_WRONG_DIMENSION_ERROR', 'CG_UCHAR4',
           'CG_BUFFER4', 'CG_UCHAR1', 'CG_POSITION12',
           'CG_POSITION13', 'CG_POSITION10', 'CG_POSITION11',
           'CG_INVALID_PROGRAM_HANDLE_ERROR', 'CG_POSITION14',
           'CG_POSITION15', 'CG_STRING', 'CG_PATCH',
           'CG_PARAMETERCLASS_ARRAY', 'CG_FALSE', 'CG_TEX3',
           'CG_TEX2', 'CG_TEX1', 'CG_TEX0', 'CG_TEX7', 'CG_TEX6',
           'CG_TEX5', 'CG_TEX4', 'CG_ARRAY',
           'CG_TESSELLATION_EVALUATION_DOMAIN', 'CG_PROGRAM_ENTRY',
           'CG_CONTROLPOINTID', 'CG_BLENDWEIGHT14',
           'CG_BLENDWEIGHT11', 'CG_BLENDWEIGHT10', 'CG_BLENDWEIGHT13',
           'CG_BLENDWEIGHT12', 'CG_HALF4x4',
           'CG_OUT_OF_ARRAY_BOUNDS_ERROR', 'CG_HALF4x1', 'CG_HALF4x2',
           'CG_HALF4x3', 'CG_PROFILE_HS_5_0', 'CG_BOOL3', 'CG_BOOL2',
           'CG_BOOL1', 'CG_TANGENT9', 'CG_PROFILE_GP4GP',
           'CG_TANGENT7', 'CG_TANGENT6', 'CG_TANGENT5', 'CG_TANGENT4',
           'CG_BOOL1x4', 'CG_TANGENT2', 'CG_TANGENT1', 'CG_TANGENT0',
           'CG_BLENDWEIGHT1', 'CG_BLENDWEIGHT0', 'CG_BLENDWEIGHT3',
           'CG_BLENDWEIGHT2', 'CG_BLENDWEIGHT5', 'CG_BLENDWEIGHT4',
           'CG_BLENDWEIGHT7', 'CG_VARYING', 'CG_BLENDWEIGHT9',
           'CG_BLENDWEIGHT8', 'CG_TEXUNIT9', 'CG_TEXUNIT8',
           'CG_NORMAL0', 'CG_NORMAL1', 'CG_NORMAL6', 'CG_NORMAL7',
           'CG_NORMAL4', 'CG_NORMAL5', 'CG_TEXUNIT1', 'CG_TEXUNIT0',
           'CG_TEXUNIT3', 'CG_TEXUNIT2', 'CG_TEXUNIT5', 'CG_TEXUNIT4',
           'CG_TEXUNIT7', 'CG_TEXUNIT6', 'CG_ATTR12', 'CG_ATTR13',
           'CG_ATTR10', 'CG_ATTR11', 'CG_ATTR14', 'CG_ATTR15',
           'CG_IS_VERTEX_PROFILE', 'CG_THREAD_SAFE_POLICY',
           'CG_SAMPLER1DSHADOW', 'CG_PROFILE_GP5FP', 'CG_UINT3x3',
           'CG_PROFILE_PS_2_SW', 'CG_PROFILE_UNKNOWN',
           'CG_INVALID_FUNCTION_HANDLE_ERROR', 'CG_PSIZ',
           'CG_UCHAR3x4', 'CG_BEHAVIOR_LATEST', 'CG_BEHAVIOR_CURRENT',
           'CG_SHORT4', 'CG_SHORT2', 'CG_SHORT3', 'CG_SHORT1',
           'CG_VERTEX', 'CG_DEPTH2', 'CG_DEPTH5', 'CG_DEPTH4',
           'CG_PROGRAM_NOT_LOADED_ERROR', 'CG_DEPTH7', 'CG_LITERAL',
           'CG_INVALID_PARAMETER_HANDLE_ERROR', 'CG_DEFAULT',
           'CG_TEXCOORD15', 'CG_BUFFER_USAGE_DYNAMIC_READ',
           'CG_STATE_ASSIGNMENT_TYPE_MISMATCH_ERROR', 'CG_LONG2x2',
           'CG_LONG2x4', '_CGprogram', 'CG_PROGRAM_BIND_ERROR',
           'CG_SHORT2x4', 'CG_FILE_WRITE_ERROR', 'CG_SHORT2x2',
           'CG_SHORT2x3', 'CG_SHORT2x1', 'CG_DOUBLE2x4',
           'CG_SAMPLE14', 'CG_DOUBLE2x1', 'CG_DOUBLE2x2',
           'CG_DOUBLE2x3', 'CG_TEXUNIT15', 'CG_TEXUNIT14',
           'CG_TEXUNIT17', 'CG_TEXUNIT16', 'CG_TEXUNIT11',
           'CG_TEXUNIT10', 'CG_TEXUNIT13', 'CG_TEXUNIT12',
           'CG_BLENDINDICES7', 'CGstatecallback', 'CG_TEXUNIT19',
           'CG_TEXUNIT18', 'CG_DUPLICATE_NAME_ERROR',
           'CG_BLENDINDICES6', 'CG_BLENDWEIGHT6', 'CG_FIXED',
           'CG_CHAR2x1', 'CG_COLUMN_MAJOR', 'CG_GLOBAL',
           'CG_BUFFER11', 'CG_BUFFER10',
           'CG_ARRAY_SIZE_MISMATCH_ERROR', 'CG_FIXED1x4', 'CG_FIXED2',
           'CG_FIXED3', 'CG_FIXED1', 'CG_FIXED4', 'CG_FLOAT3x2',
           'CG_FIXED1x1', 'CG_POINTCOORD', 'CG_FIXED1x3',
           'CG_FIXED1x2', 'CG_FLOAT3x1', 'CG_PSIZE8']
