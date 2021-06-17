import os
from PyQt5 import QtWidgets,QtCore
from numpy import nan
class READ_THE_STDF_FILE():
    '''This Class is used to Read the STDF File.
    Its has all the records an STDF file contains and Will store the data of all records together'''
    # Defining_variables
    odd_nibble=True
    Lists_in_Temp_Rec_Summary_are_empty=False
    Record_Number=0
    File_Load_Status=QtCore.pyqtSignal(int)
    All_Record_Names={}
    All_Record_Names[0,10]=['FAR']
    All_Record_Names[0,20]=['ATR']
    All_Record_Names[0,30]=['VUR']
    All_Record_Names[1,10]=['MIR']
    All_Record_Names[1,20]=['MRR']
    All_Record_Names[1,30]=['PCR']
    All_Record_Names[1,40]=['HBR']
    All_Record_Names[1,50]=['SBR']
    All_Record_Names[1,60]=['PMR']
    All_Record_Names[1,62]=['PGR']
    All_Record_Names[1,63]=['PLR']
    All_Record_Names[1,70]=['RDR']
    All_Record_Names[1,80]=['SDR']
    All_Record_Names[1,90]=['PSR']
    All_Record_Names[1,91]=['NMR']
    All_Record_Names[1,92]=['CNR']
    All_Record_Names[1,93]=['SSR']
    All_Record_Names[1,94]=['SCR']
    All_Record_Names[2,10]=['WIR']
    All_Record_Names[2,20]=['WRR']
    All_Record_Names[2,30]=['WCR']
    All_Record_Names[5,10]=['PIR']
    All_Record_Names[5,20]=['PRR']
    All_Record_Names[10,30]=['TSR']
    All_Record_Names[15,10]=['PTR']
    All_Record_Names[15,15]=['MPR']
    All_Record_Names[15,20]=['FTR']
    All_Record_Names[15,30]=['STR']
    All_Record_Names[20,10]=['BPS']
    All_Record_Names[20,20]=['EPS']
    All_Record_Names[50,10]=['GDR']
    All_Record_Names[50,30]=['DTR']
    ## Main Program Starts with initialisation
    def __init__(self,parent=None): #,Input_File
        ''' init Will take the STDF file as input and Reads the Data in it.'''
        # Defining the Dict's
        self.test=5
        self.Parent_Window=parent
        self.Record_summary_list=['FAR_Rec_Summary','ATR_Rec_Summary','MIR_Rec_Summary','SDR_Rec_Summary','PMR_Rec_Summary',
                                'WCR_Rec_Summary','WIR_Rec_Summary','PIR_Rec_Summary','PRR_Rec_Summary','MPR_Rec_Summary','WRR_Rec_Summary','TSR_Rec_Summary',
                                'HBR_Rec_Summary','SBR_Rec_Summary','PCR_Rec_Summary','MRR_Rec_Summary','BPS_Rec_Summary','DTR_Rec_Summary','PGR_Rec_Summary',
                                'RDR_Rec_Summary','GDR_Rec_Summary']
        self.FAR_Rec_Summary={"File_Name":[],"CPU_TYPE":[],"STDF_VER":[]}
        self.ATR_Rec_Summary={"File_Name":[],'MOD_TIM':[],'CMD_Line':[]}
        self.MIR_Rec_Summary={"File_Name":[],'Setuptime':[],'Strtuptime':[],'Stat_Num':[],'modcode':[],'retestcode':[],'protcode':[],'Burntime':[],'cmodcode':[],'Lotid':[],'Parttype':[],'NodName':[],'TesterType':[],'Jobname':[],'Jobrev':[]
                            ,'Sublotid':[],'Opername':[],'ExSwtype':[],'ExSwver':[],'TestCode':[],'TestTemp':[],'GenUTest':[],'AuxDfile':[],'Pcktyp':[],'PFid':[],'DateCode':[],
                            'FacilId':[],'FloorId':[],'FabPId':[],'OpFreq':[],'TestSpecVerName':[],'FlowId':[],'SetupId':[],'DDrev':[],'EnggId':[],'RomCode':[],'Serl_Num':[],'Supr_Nam':[]}
        self.SDR_Rec_Summary={'File_Name':[],'Testheadnumber':[],'SiteGroup':[],'Number_Of_Sites':[],'SiteNumber':[],'Handlertype':[],'HandlerId':[],'CardType':[],'CardId':[],
                            'LoadBrdType':[],'LoadBrdId':[],'DibBrdTyp':[],'DibBrdId':[],'Intefctyp':[],'InterfaceId':[],'HandlerContType':[],'HandlerContId':[],'LaserType':[],'LaserId':[],
                            'ExtraEQtype':[],'ExtraEQId':[]}
        self.PMR_Rec_Summary={"File_Name":[],'UIndex':[],'ChanelType':[],'ChanelName':[],'PhNameOfPin':[],'LocalNameofPin':[],'HeadNumber':[],'SiteNumber':[]}
        self.WCR_Rec_Summary={"File_Name":[],'WaferSize':[],'DiHight':[],'DieWidht':[],'WaferUnits':[],'Wflat':[],'X_Co':[],'Y_Co':[],'POS_X':[],'POS_Y':[]}
        self.WIR_Rec_Summary={"File_Name":[],'TestHeadnumber':[],'SiteGourpNumber':[],'DateEndTime':[],'WfrId':[]}        
        self.PIR_Rec_Summary={"File_Name":[],'TestHeadnumber':[],'TestSiteNumber':[]}
        self.PRR_Rec_Summary={"File_Name":[],'HeadNum':[],'SiteNum':[],'Part_Flag':[],'Num_Test':[],'HardBin':[],'SoftBin':[],'Hbin_Num:Name':[],'Sbin_Num:Name':[],'XCo_ord':[],'YCo_ord':[],'Testtime':[],'PartId':[],'Part_Dis_Txt':[],'PartFix':[],'IsNewPart':[],'Abnormal_end_of_testing':[],'Device_info':[]}
        self.WRR_Rec_Summary={"File_Name":[],'HeadNum':[],'Site_Grp':[],'Finish_t':[],'Part_Cnt':[],'Rtst_Cnt':[],'Abrt_cnt':[],'Good_cnt':[],'Func_Cnt':[],'Wafer_id':[],'Fabwf_id':[],'Frame_id':[],'Mask_id':[],'Usr_desc':[],'Exc_Desc':[]}
        self.TSR_Rec_Summary={"File_Name":[],'HeadNum':[],'SiteNum':[],'Test_type':[],'TestNumber':[],'Exec_Cnt':[],'Fail_Cnt':[],'Alarm_Cnt':[],'Test_nam':[],'Seq_nam':[],'Test_lbl':[],'Opt_Flag':[],'Test_tim':[],'Test_min':[],'Test_max':[],'Test_sums':[],'Test_sqrs':[],'Record_number':[]}
        self.HBR_Rec_Summary={"File_Name":[],'HeadNum':[],'SiteNum':[],'HbinNum':[],'Hbin_Cnt':[],'Hbin_Pf':[],'Hbin_nam':[]}
        self.SBR_Rec_Summary={"File_Name":[],'HeadNum':[],'SiteNum':[],'SbinNum':[],'Sbin_Cnt':[],'Sbin_Pf':[],'Sbin_nam':[]}
        self.PCR_Rec_Summary={"File_Name":[],'HeadNum':[],'SiteNum':[],'Part_cnt':[],'Rtst_Cnt':[],'Abrt_Cnt':[],'Good_Cnt':[],'Func_Cnt':[]}
        self.MRR_Rec_Summary={"File_Name":[],'Finist_Time':[],'Disp_Cod':[],'USr_Desc':[],'Exc_Desc':[]}
        self.BPS_Rec_Summary={"File_Name":[],'Seq_name':[]}
        self.DTR_Rec_Summary={"File_Name":[],'TEXT_DAT':[]}
        self.PGR_Rec_Summary={"File_Name":[],'Grp_index':[],'GRP_NAM':[],'INDX_CNT':[],'PMR_INDX_str':[]}
        self.RDR_Rec_Summary={"File_Name":[],'Num_bins':[],'RTST_BIN_str':[]}
        self.GDR_Rec_Summary={"File_Name":[],'Fld_Cnt':[],'GDR_Summary_str':[]}
        self.VUR_Rec_Summary={"File_Name":[],'UPD_NAM':[]}
        self.PSR_Rec_Summary={"File_Name":[],'CONT_FLG':[],'PSR_INDX':[],'PSR_NAM':[],'OPT_FLG':[],'TOTP_CNT':[],'LOCP_CNT':[]}
        self.NMR_Rec_Summary={"File_Name":[],'CONT_FLG':[],'TOTM_CNT':[],'LOCM_CNT':[],'PMR_INDX':[],'ATPG_NAM':[]}
        self.CNR_Rec_Summary={"File_Name":[],'CHN_NUM':[],'BIT_POS':[],'CELL_NAM':[]}
        self.SSR_Rec_Summary={"File_Name":[],'SSR_NAM':[],'CHN_CNT':[],'CHN_LIST':[]}
        self.SCR_Rec_Summary={"File_Name":[],'CONT_FLG':[],'CDR_INDX':[],'CHN_NAM':[],'CHN_LEN':[],'SIN_PIN':[],'SOUT_PIN':[],'MSTR_CNT':[],'M_CLKS':[],'SLAV_CNT':[],'S_CLKS':[],'INV_VAL':[],'LST_CNT':[],'CELL_LST':[]}
        self.STR_Rec_Summary={"File_Name":[],'CONT_FLG':[],'TEST_NUM':[],'HEAD_NUM':[],'SITE_NUM':[],'PSR_REF':[],'TEST_FLG':[],'LOG_TYP':[],'TEST_TXT':[],'ALARM_ID':[],'PROG_TXT':[],'RSLT_TXT':[],'Z_VAL':[],'FMU_FLG':[],'MASK_MAP':[],'FAL_MAP':[],'CYC_CNT':[],'TOTF_CNT':[],'TOTL_CNT':[],'CYC_BASE':[]
                            ,'BIT_BASE':[],'COND_CNT':[],'LIM_CNT':[],'CYC_SIZE':[],'PMR_SIZE':[],'CHN_SIZE':[],'PAT_SIZE':[],'BIT_SIZE':[],'U1_SIZE':[],'U2_SIZE':[],'U3_SIZE':[],'UTX_SIZE':[],'CAP_BGN':[],'LIM_INDX':[],'LIM_SPEC':[],'COND_LST':[],'CYC_CNT2':[],'CYC_OFST':[],'PMR_CNT':[],'PMR_INDX':[],'CHN_CNT':[]
                            ,'CHN_NUM':[],'EXP_CNT':[],'EXP_DATA':[],'CAP_CNT':[],'CAP_DATA':[],'NEW_CNT':[],'NEW_DATA':[],'PAT_CNT':[],'PAT_NUM':[],'BPOS_CNT':[],'BIT_POS':[],'USR1_CNT':[],'USR1':[],'USR2_CNT':[],'USR2':[],'USR3_CNT':[],'USR3':[],'TXT_CNT':[],'USER_TXT':[]}
        self.Test_Details={'000':['TestNumber' ,'TestName' ,'LowLimit' ,'HighLimit', 'Unit']}
        self.Test_Flag_Details={'000':['OptFlag','TestResultScalingExpo','LowLimitScalingExpo','HighLimitScalingExpo','LowLimit','HighLim','TestUnit','C_Result_Fmt_String','C_low_lim_fmt_string','C_High_Lim_Fmt_string','Low_spec','High_Spec']}
        self.TestNumbers={}
        self.FullTestDetails=['TestFull details']
        self.PartFullInfo=[[['Part_Number','','','','']],[['TestHeadNumber',' ',' ',' ',' ']],[['SiteNumber',' ',' ',' ',' ']],[['PartFlag',' ',' ',' ',' ']],[['NumberofTestesExcicuted',' ',' ',' ',' ']],[['HardBin',' ',' ',' ',' ']],[['Softbin',' ',' ',' ',' ']],[['X co',' ',' ',' ',' ']],[['Y co',' ',' ',' ',' ']]]
        self.PTR_Rec_Summary={'File_Name':[],'Record_number':[],'TestNumber':[],'TestHeadNumber':[],'TestSiteNumber':[],'TestFlag':[],'Paramatric_flag':[],'Result':[],
                            'Test_Txt':[],'Alaram_Id':[],'Opt_flag':[],'Res_Scal':[],'Llm_Scal':[],'Hlm_Scal':[],'Lo_limit':[],'Hi_limit':[],'Units':[],'C_RESFMT':[],'c_LLMFMT':[],'C_HLMFMT':[],'LO_SPEC':[],'HI_SPEC':[],
                            'Alarm_Detected_during_testing':[],'Test_result_is_valid':[],'Test_result_is_reliable':[],'Time_out_occured':[],'Test_exicuted':[],'Test_aborted':[],'Test_passed':[],'Scale_Error':[],
                            'Drift_Error':[],'Oscillation_detected':[],'Measured_value_Higher_than_High_test_limit':[],'Measured_value_Lower_than_Low_test_limit':[],'Test_Pass_Fail':[],'Failed_at_low_lim':[],'Failed_at_high_lim':[]}
        self.MPR_Rec_Summary={"File_Name":[],'Record_number':[],'TestNumber':[],'TestHeadNumber':[],'SiteNumber':[],'TestFlag':[],'ParamFlag':[],'Rtn_Icnt':[],'Rslt_cnt':[],'Rtn_Stat_str':[],'TestResult_str':[],'TestName':[],'AlaramName':[],'OptFlag':[],'TRSE':[],'LLSE':[],'HLSE':[],'LowLim':[],'HighLim':[],'Start_in':[],'Incr_in':[],'Rtn_indx_str':[],'TestUnit':[],'Units_in':[],'CRFS':[],'CLLFS':[],'CHLFS':[],'LowSpec':[],'HighSpec':[],
                            'Alarm_Detected_during_testing':[],'Test_result_is_reliable':[],'Time_out_occured':[],'Test_exicuted':[],'Test_aborted':[],'Test_passed':[],'Scale_Error':[],
                            'Drift_Error':[],'Oscillation_detected':[],'Measured_value_Higher_than_High_test_limit':[],'Measured_value_Lower_than_Low_test_limit':[],'Test_Pass_Fail':[],'Failed_at_low_lim':[],'Failed_at_high_lim':[]}
        self.FTR_Rec_Summary={'File_Name':[],'Record_number':[],'TestNumber':[],'TestHeadNumber':[],'SiteNumber':[],'TestFlag':[],'OptFlag':[],'Cycl_Cnt':[],'Rel_V_Addr':[],'Rept_C_Vctr':[],'Num_P_Fail':[],
                                'X_Fail_Adrs':[],'Y_Fail_Adrs':[],'Vect_offset':[],'Rtn_PmrIndex_cnt':[],'Pgm_StateIndex':[],'RTN_Index_ary_str':[],'RTN_State_ary_str':[],'Pgm_State_indx_ary_str':[],'Pgm_State_ary_str':[],'Failpin':[],'VectNum':[],'Timesetname':[],'opcode':[],'Test_Txt':[],'AlrmId':[],'ProgmTxt':[],'RsltTxt':[],'Patrn_num':[],'SpinMap':[],'Alarm_Detected_during_testing':[],'Test_result_is_reliable':[],'Time_out_occured':[],'Test_exicuted':[],'Test_aborted':[],'Test_passed':[]}
        self.Record_Details_list=[["Recrod Number"],['Record Name'],['Some Details of the record']]
        self.Full_Rec_Summary={"File_Name":[],'Setuptime':[],'Strtuptime':[],'Stat_Num':[],'modcode':[],'retestcode':[],'protcode':[],'Burntime':[],'Lotid':[],'Parttype':[],'NodName':[],'TesterType':[],'Jobname':[],'Jobrev':[]
                                ,'Sublotid':[],'Opername':[],'TestTemp':[],'FlowId':[],'SetupId':[],'RomCode':[],'TestHeadnumber':[],'TestSiteNumber':[],'Part_Flag':[],'Num_Test':[],'HardBin':[],'Hbin_nam':[],'SoftBin':[],'Sbin_nam':[],'XCo_ord':[],'YCo_ord':[],'Testtime':[],'PartId':[],'Part_Dis_Txt':[],'PartFix':[],'IsNewPart':[],'Hbin_Num:Name':[],'Sbin_Num:Name':[],'Re-test':[]}
        self.Temp_Rec_Summary={"File_Name":[],'Setuptime':[],'Strtuptime':[],'Stat_Num':[],'modcode':[],'retestcode':[],'protcode':[],'Burntime':[],'Lotid':[],'Parttype':[],'NodName':[],'TesterType':[],'Jobname':[],'Jobrev':[]
                                ,'Sublotid':[],'Opername':[],'TestTemp':[],'FlowId':[],'SetupId':[],'RomCode':[],'TestHeadnumber':[],'TestSiteNumber':[],'Part_Flag':[],'Num_Test':[],'HardBin':[],'Hbin_nam':[],'SoftBin':[],'Sbin_nam':[],'XCo_ord':[],'YCo_ord':[],'Testtime':[],'PartId':[],'Part_Dis_Txt':[],'PartFix':[],'IsNewPart':[],'Hbin_Num:Name':[],'Sbin_Num:Name':[],'Re-test':[]}
        #Full_FIELD_LIST=[['File_Name',],['Setuptime',],['Strtuptime',],['Stat_Num',],['modcode',],['retestcode',],['protcode',],['Burntime',],['Lotid',],['Parttype',],['NodName',],['TesterType',],['Jobname',],['Jobrev',]
        #   ,['Sublotid',],['Opername',],['TestTemp',],['FlowId',],['SetupId',],['RomCode',],['TestHeadnumber',],['TestSiteNumber',],['Part_Flag',],['Num_Test',],['HardBin',],['Hbin_nam',],['SoftBin',],['Sbin_nam',],['XCo_ord',],['YCo_ord',]]
        #Record_summary_list2=[FAR_Rec_summary,ATR_Rec_summary,MIR_Rec_Summary,SDR_Rec_Summary,PMR_Rec_Summary]
        self.Full_FIELD_LIST=['File_Name','Setuptime','Strtuptime','Stat_Num','modcode','retestcode','protcode','Burntime','Lotid','Parttype','NodName','TesterType','Jobname','Jobrev','Sublotid','Opername','TestTemp','FlowId','SetupId','RomCode','TestHeadnumber','TestSiteNumber','Re-test','Part_Flag','Num_Test','HardBin','Hbin_nam','SoftBin','Sbin_nam','IsNewPart','Hbin_Num:Name','Sbin_Num:Name','XCo_ord','YCo_ord','Testtime','PartId','Part_Dis_Txt','PartFix']
        self.Test_Limit_Details={"TestNumber;Name":["Low_Lim","High_Lim","Unit"]}
        self.Part_id_Index={}
        self.Clubbed_Record_Details=[self.FAR_Rec_Summary,self.ATR_Rec_Summary,self.MIR_Rec_Summary,self.SDR_Rec_Summary,
        self.PMR_Rec_Summary,self.WCR_Rec_Summary,self.WIR_Rec_Summary,self.PIR_Rec_Summary,self.PRR_Rec_Summary,
        self.MPR_Rec_Summary,self.WRR_Rec_Summary,self.TSR_Rec_Summary,self.HBR_Rec_Summary,self.SBR_Rec_Summary,
        self.PCR_Rec_Summary,self.MRR_Rec_Summary,self.BPS_Rec_Summary,self.DTR_Rec_Summary,self.PGR_Rec_Summary,
        self.RDR_Rec_Summary,self.GDR_Rec_Summary,self.Test_Details,self.Test_Flag_Details,self.PTR_Rec_Summary,
        self.FTR_Rec_Summary,self.Full_Rec_Summary,self.Test_Limit_Details]
        self.TSR_Final_Test_details=[[],[],[]]
        self.struct=__import__('struct')
        self.math=__import__('math')
        self.sys=__import__('sys')
        #self.xlsxwriter=__import__('xlsxwriter')
        #self.pandas=__import__('pandas')        
        #Starting_byte=0
        self.Next_Reading_Byte=0
        self.Record_lenght=0
        self.Record_Name='Null'
        self.End_Record_Byte=0
        self.Number_Of_Sites=0
        self.Record_name="DontKnow"
        self.PLR_Rec_Summary=""
        #Scaling methods
        self.Scale_values={15:['f','femto',-15],12:['p','pico', -12],9:['n', 'nano', -9],6:['u', 'micro', -6],3:['m' ,'milli', -3],2:['%' ,'percent', -2],0: ['', '', 0],
        -3:['K','Kilo', 3],-6:['M','Mega', 6],-9:['G','Giga',9],-12:['T','Tera',12]}
        #Creating the Dictionry for Records
    #Declaring some variables for further use age
    #global Starting_byte
    #global Next_Reading_Byte,Record_lenght,Record_Name,End_Record_Byte,Number_Of_Sites,Record_name
    #Supporting functions
    # Uncoding Data Types and Encoding different records  
    def U1(self,Starting_byte,Length_of_char): return self.struct.unpack(str(Length_of_char)+'B',self.STDF_Data[Starting_byte:Starting_byte+Length_of_char])[0], Starting_byte+Length_of_char
    def I1(self,Starting_byte,Length_of_char):return self.struct.unpack(str(Length_of_char)+'b',self.STDF_Data[Starting_byte:Starting_byte+Length_of_char])[0], Starting_byte+Length_of_char
    def KX_One_Byte_Unsingned_int(self,Starting_byte,K_values):
        K=K_values;return self.struct.unpack(str(K)+'B',self.STDF_Data[Starting_byte:Starting_byte+int(K)])[0], Starting_byte+int(K)
    def U2(self,Starting_byte,Length_of_char):return self.struct.unpack(str(Length_of_char)+'H',self.STDF_Data[Starting_byte:Starting_byte+(2*Length_of_char)])[0],Starting_byte+(2*Length_of_char)
    def I2(self,Starting_byte,Length_of_char):return self.struct.unpack(str(Length_of_char)+'h',self.STDF_Data[Starting_byte:Starting_byte+(2*Length_of_char)])[0], Starting_byte+(2*Length_of_char)
    def R4(self,Starting_byte,Length_of_char):return self.struct.unpack(str(Length_of_char)+'f',self.STDF_Data[Starting_byte:Starting_byte+(4*Length_of_char)])[0], Starting_byte+(4*Length_of_char)
    def U4(self,Starting_byte,Length_of_char):return self.struct.unpack(str(Length_of_char)+'I',self.STDF_Data[Starting_byte:Starting_byte+(4*Length_of_char)])[0], Starting_byte+(4*Length_of_char)
    def U8(self,Starting_byte,Length_of_char):return self.struct.unpack(str(Length_of_char)+'Q',self.STDF_Data[Starting_byte:Starting_byte+(8*Length_of_char)])[0], Starting_byte+(8*Length_of_char)
    def I4(self,Starting_byte,Length_of_char):return self.struct.unpack(str(Length_of_char)+'i',self.STDF_Data[Starting_byte:Starting_byte+(4*Length_of_char)])[0], Starting_byte+(4*Length_of_char)
    def R8(self,Starting_byte,Length_of_char):return self.struct.unpack(str(Length_of_char)+'d',self.STDF_Data[Starting_byte:Starting_byte+(8*Length_of_char)])[0], Starting_byte+(8*Length_of_char)
    def C1(self,Starting_byte,Length_of_char):return self.struct.unpack(str(Length_of_char)+'c',self.STDF_Data[Starting_byte:Starting_byte+Length_of_char])[0].decode("utf-8"), Starting_byte+Length_of_char
    def B1(self,Starting_byte,Bytelenght):return bin(self.struct.unpack(str(Bytelenght)+'s',self.STDF_Data[Starting_byte:Starting_byte+1])[0][0])[2:].zfill(8),Starting_byte+1
    def DN(self,Starting_byte,Length_of_char):
        x,Starting_byte=self.U2(Starting_byte,1)#;print(x[0])
        x=self.math.ceil(x/8)
        if x>0:
            x,Starting_byte=self.U1(Starting_byte,x);y=str(x);x=' '.join(format(ord(i), 'b') for i in y)#print(y);x=format(ord(y),'b');lth=len(x)-1;x=x[lth:]#x=''.join(format(ord(i),'b') for i in y)#
            return x,Starting_byte  
        else:
            return x,Starting_byte
    def BN(self,Starting_byte,Lenght_of_Char):
        Nextbyte,Starting_byte=self.U1(Starting_byte,1)
        #print(Starting_byte)
        if Nextbyte>0:
            x,Starting_byte=self.U1(Starting_byte, Nextbyte);return x,Starting_byte
        elif Nextbyte==0:
            return Nextbyte,Starting_byte
    def B0(self,Starting_byte):print('B0 not defined')        
    def CN(self,Starting_byte,Length_of_char):
        ''' Reads the Variable lenght char data, C*n data type of STDF from the given data.'''
        Byte_length_of_field,Starting_byte=self.U1(Starting_byte,1)
        if Byte_length_of_field>0:
            dumy=self.struct.unpack(str(Byte_length_of_field) +'s',self.STDF_Data[Starting_byte:Starting_byte+Byte_length_of_field])[0].decode('utf-8')
            return dumy, Starting_byte+Byte_length_of_field
        elif Byte_length_of_field==0:
            Field=''#;print('Field Empty :',Field)
            return Field,Starting_byte+Byte_length_of_field
    def SN(self,Starting_byte,Length_of_char):
        ''' Reads the Variable lenght char data, C*n data type of STDF from the given data.'''
        Byte_length_of_field,Starting_byte=self.U2(Starting_byte,1)
        if Byte_length_of_field>0:
            dumy=self.struct.unpack(str(Byte_length_of_field) +'s',self.STDF_Data[Starting_byte:Starting_byte+Byte_length_of_field])[0].decode('utf-8')
            return dumy, Starting_byte+Byte_length_of_field
        elif Byte_length_of_field==0:
            Field=''#;print('Field Empty :',Field)
            return Field,Starting_byte+Byte_length_of_field
    def N1(self,Starting_byte,Lenght_of_Char):
        if self.odd_nibble==True:
            nibble,=self.struct.unpack("<B",self.STDF_Data[Starting_byte:Starting_byte+1]);Starting_byte+=1
            _,dat=nibble >> 4,nibble & 0xF
            self.odd_nibble=False#;data.append(dat)
        else:
            nibble,=self.struct.unpack("<B",self.STDF_Data[Starting_byte-1:Starting_byte])
            dat,_=nibble >>4,nibble & 0xF
            self.odd_nibble=True#;data.append(dat)
        return dat,Starting_byte
    def Missing_Invalid_Data(self,Starting_byte,TestNumber,Rec_summary_name,Txt):
        if Starting_byte<self.End_Record_Byte:
            byte_length,Starting_byte=self.U1(Starting_byte,1);Variable_Name=''
            if TestNumber!='':
                if byte_length==0 and TestNumber in Rec_summary_name['TestNumber']:
                    Variable_Name=Rec_summary_name[Txt][Rec_summary_name['TestNumber'].index(TestNumber)]        
                elif byte_length!=0 or byte_length>0:
                    Starting_byte-=1
                    Variable_Name,Starting_byte=self.CN(Starting_byte,1)#;print('Test Discription:',TestName)
                return Variable_Name,Starting_byte
            elif TestNumber=='':                
                if byte_length!=0 or byte_length>0:
                    Starting_byte-=1
                    Variable_Name,Starting_byte=self.CN(Starting_byte,1)#;print('Test Discription:',TestName)
                return Variable_Name,Starting_byte
        else:
            return '',Starting_byte
    def KX_Looped_data(self,Starting_byte,Decoding_Data_type,Loop_constant,index_byte):
        Looped_data=[]
        if Decoding_Data_type!= self.UF:
            if (Loop_constant==1 and Loop_constant!=0): Looped_data,Starting_byte=Decoding_Data_type(Starting_byte,1);Looped_data=[Looped_data]
            elif Loop_constant>1:                
                for i in range(0,Loop_constant): Array_val,Starting_byte=Decoding_Data_type(Starting_byte,1);Looped_data.append(Array_val)
        elif Decoding_Data_type== self.UF:
            if (Loop_constant==1 and Loop_constant!=0): Looped_data,Starting_byte=Decoding_Data_type(Starting_byte,1,index_byte);Looped_data=[Looped_data]
            elif Loop_constant>1:                
                for i in range(0,Loop_constant): Array_val,Starting_byte=Decoding_Data_type(Starting_byte,1,index_byte);Looped_data.append(Array_val)
        return Looped_data,Starting_byte
    def UF(self,Starting_byte,Length_of_char,index_byte):
        if index_byte<=8 and index_byte>0:
            return (self.U1(Starting_byte,Length_of_char) if index_byte<2 else self.U2(Starting_byte,Length_of_char)) if index_byte<=2 else (self.U4(Starting_byte,Length_of_char) if index_byte==4 else self.U8(Starting_byte,Length_of_char))
    def Zero_len_byte(self,Starting_byte,decoding_type):
            if Starting_byte<=self.End_Record_Byte: return decoding_type(Starting_byte,1)
            else:  return '',Starting_byte
    VN_MAP={'0':B0,'1':U1,'2':U2,'3':U4,'4':I1,'5':I2,'6':I4,'7':R4,'8':R8,'10':CN,'11':BN,'12':DN,'13':N1}
    #Get the Input File
    def Load_the_file(self,Input_file):
         #global self.STDF_Data
        self.STDF_File=open(Input_file,'rb')
        self.STDF_Data=self.STDF_File.read()
    #Type record
    def Record_header(self,Starting_byte):
        ''' Reads the Record header of the data, Record length, Record type and Record sub type.
            Caliculates the End Byte of the Record. And gets the What is Record being decoded next.'''
        #global self.End_Record_Byte
        self.Rec_len,Starting_byte=self.U2(Starting_byte,1)
        self.Rec_type,Starting_byte=self.U1(Starting_byte,1)
        self.Rec_sub_type,Starting_byte=self.U1(Starting_byte,1)
        self.Record_name_key=(self.Rec_type,self.Rec_sub_type)
        self.End_Record_Byte=Starting_byte+self.Rec_len        
        self.Record_name=self.All_Record_Names[self.Record_name_key]
        self.Record_Number+=1
        self.Record_Details_list[0].append(self.Record_Number)
        #print(self.Record_Number)
        self.Record_Details_list[1].append(self.Record_name[0])
        return Starting_byte
    #Functions for getting the records & its data
    def FAR(self,Starting_byte):
        '''Reads the File Attribute Record(FAR) from the STDF.'''
        self.CPU_TYPE,Starting_byte=self.U1(Starting_byte,1)
        self.STDF_VER,Starting_byte=self.U1(Starting_byte,1)        
        self.FAR_Rec_Summary["CPU_TYPE"].append(self.CPU_TYPE);self.FAR_Rec_Summary["STDF_VER"].append(self.STDF_VER);self.FAR_Rec_Summary["File_Name"].append(self.STDF_File.name)
        return Starting_byte
    def ATR(self,Starting_byte):
        ''' Reads the Audit Trail record from the STDF.'''
        MOD_TIM,Starting_byte=self.U4(Starting_byte,1)
        CMD_Line,Starting_byte=self.CN(Starting_byte,1)
        self.ATR_FIELD_LIST=[['MOD_TIM',MOD_TIM],['CMD_Line',CMD_Line]]                
        self.ATR_Rec_Summary['File_Name'].append(self.STDF_File.name);self.ATR_Rec_Summary['MOD_TIM'].append(MOD_TIM);self.ATR_Rec_Summary['CMD_Line'].append(CMD_Line)
        return Starting_byte
    def MIR(self,Starting_byte):
        ''' Reads the Master Information record (MIR) from the stdf.'''    
        Setuptime,Starting_byte=self.U4(Starting_byte,1)#;print('Setup time',Setuptime[0])
        Strtuptime,Starting_byte=self.U4(Starting_byte,1)#;print('Start up time',Strtuptime[0])	
        Stat_Num,Starting_byte=self.U1(Starting_byte,1)#;print('STAT NUM',Stat_Num[0])
        modcode,Starting_byte=self.C1(Starting_byte,1)
        retestcode,Starting_byte=self.C1(Starting_byte,1)
        protcode,Starting_byte=self.C1(Starting_byte,1)
        Burntime,Starting_byte=self.U2(Starting_byte,1)#;print('BURN TIME',Burntime[0])	
        cmodcode,Starting_byte=self.C1(Starting_byte,1)
        Lotid,Starting_byte=self.CN(Starting_byte,1)#;print('LOT ID',Lotid[0])
        Parttype,Starting_byte=self.CN(Starting_byte,1)#;print('PART_TYP',Parttype[0])
        NodName,Starting_byte=self.CN(Starting_byte,1)#;print('NODE_NAM',NodName[0])
        TesterType,Starting_byte=self.CN(Starting_byte,1)#;print('TESTER_TYPE',TesterType[0])
        Jobname,Starting_byte=self.CN(Starting_byte,1)#;print('JOB_NAME',Jobname[0])
        Jobrev,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')#;print('JOB_REVISION',Jobrev[0])
        Sublotid,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')#;print('SUBLOT_ID',Sublotid)
        Opername,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')#;print('OPERATOR_NAME',Opername[0])
        ExSwtype,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')#;print('EXECUTIVE SW TYPE',ExSwtype[0])
        ExSwver,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')#;print('EXECUTIVE SW VER NUM',ExSwver[0])
        TestCode,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')#;print('TEST CODE',TestCode)
        TestTemp,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')#;print('TEST TEMPRATURE',TestTemp)
        GenUTest,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')#;print('GENERIC USER TEXT',GenUTest)
        AuxDfile,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')#;print('AUXILIARY DATA FILE',AuxDfile)
        Pcktyp,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')#;print('PACKAGE TYPE',Pcktyp)
        PFid,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')#;print('PRODUCT FAMILY ID',PFid) 
        DateCode,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')#;print('DATE CODE',DateCode)
        FacilId,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')#;print('FACIL_ID',FacilId) 
        FloorId,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')#;print('FLOOR_ID',FloriId)	
        FabPId,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')#;print('FAB_PROCESS_ID',FabPId)
        OpFreq,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')#;print('OPERATION FREQ',OpFreq)  
        TestSpecVerName,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')#;print('TEST SPEC VER NAME',TestSpecVerName) 
        FlowId,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')#;print('FLOW ID',FlowId) 
        SetupId,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')#;print('SETUP ID',SetupId)  
        DDrev,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')#;print('DEVICE DESIGN REVI',DDrev) 
        EnggId,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')#;print('ENGG ID',EnggId) 
        RomCode,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')#;print('ROM CODE ID',RomCode)
        Serl_Num,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')
        Supr_Nam,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'')
        Starting_byte=self.End_Record_Byte
        self.MIR_FIELD_LIST=[['File_Name',self.STDF_File.name],['Setuptime',Setuptime],['Strtuptime',Strtuptime],['Stat_Num',Stat_Num],['modcode',modcode],['retestcode',retestcode],['protcode',protcode],['Burntime',Burntime],
        ['cmodcode',cmodcode],['Lotid',Lotid],['Parttype',Parttype],['NodName',NodName],['TesterType',TesterType],['Jobname',Jobname],['Jobrev',Jobrev],['Sublotid',Sublotid],['Opername',Opername],['ExSwtype',ExSwtype],['ExSwver',ExSwver],['TestCode',TestCode],['TestTemp',TestTemp],['GenUTest',GenUTest],['AuxDfile',AuxDfile],
        ['Pcktyp',Pcktyp],['PFid',PFid],['DateCode',DateCode],['FacilId',FacilId],['FloorId',FloorId],['FabPId',FabPId],['OpFreq',OpFreq],['TestSpecVerName',TestSpecVerName],['FlowId',FlowId],['SetupId',SetupId],['DDrev',DDrev],['EnggId',EnggId],['RomCode',RomCode],['Serl_Num',Serl_Num],['Supr_Nam',Supr_Nam]]
        for i in range(len(self.MIR_FIELD_LIST)): self.MIR_Rec_Summary[self.MIR_FIELD_LIST[i][0]].append(self.MIR_FIELD_LIST[i][1])        
        return Starting_byte 
    def SDR(self,Starting_byte):
        ''' Reads the Site Discritpiton (SDR) record from the stdf.'''    
        #global Number_Of_Sites
        self.Testheadnumber,Starting_byte=self.U1(Starting_byte,1)##;print('Test Head number :',Testheadnumber[0])
        self.SiteGroup,Starting_byte=self.U1(Starting_byte,1)#;print('Site group :',SiteGroup[0])
        self.Number_Of_Sites,Starting_byte=self.U1(Starting_byte,1)        
        if (self.Number_Of_Sites==1 and self.Number_Of_Sites!=0): self.SiteNumber,Starting_byte=self.U1(Starting_byte,1);self.SiteNumbers_string=str(self.SiteNumber)
        elif self.Number_Of_Sites>1:
            self.SiteNumber=[]
            self.SiteNumbers_string=''
            for i in range(0,self.Number_Of_Sites): Array_val,Starting_byte=self.U1(Starting_byte,1);self.SiteNumber.append(Array_val);self.SiteNumbers_string+= " "+str(Array_val)
        self.Handlertype,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print("Handler type / Prober Type :",Handlertype)
        self.HandlerId,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print("Handler ID / Prober ID :",HandlerId )
        self.CardType,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print("Card Type :",CardType)
        self.CardId,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print("Card ID :",CardId )
        self.LoadBrdType,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print("Load Board Type :",LoadBrdType)
        self.LoadBrdId,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print("Load Board ID:",LoadBrdId )
        self.DibBrdTyp,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print("DIB Board Type :",DibBrdTyp)
        self.DibBrdId,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print("DIB Board ID :",DibBrdId)
        self.Intefctyp,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print("Interface Cable Type :",Intefctyp)
        self.InterfaceId,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#; print("Interface Cable ID :",InterfaceId)
        self.HandlerContType,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print("Handler Contacter Type :",HandlerContType)
        self.HandlerContId,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print("Handler contacter ID :",HandlerContId)
        self.LaserType,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print("Laser Type :",LaserType)
        self.LaserId,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print("Laser ID :",LaserId)
        self.ExtraEQtype,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print("Extra Equipment Type :",ExtraEQtype)
        self.ExtraEQId,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print("Extra Equipment ID :")
        self.SDR_FIELD_LIST=[['File_Name',self.STDF_File.name],['Testheadnumber',self.Testheadnumber],['SiteGroup',self.SiteGroup],['Number_Of_Sites',self.Number_Of_Sites],
        ['SiteNumber',self.SiteNumbers_string],['Handlertype',self.Handlertype],['HandlerId',self.HandlerId],['CardType',self.CardType],['CardId',self.CardId],
        ['LoadBrdType',self.LoadBrdType],['LoadBrdId',self.LoadBrdId],['DibBrdTyp',self.DibBrdTyp],['DibBrdId',self.DibBrdId],['Intefctyp',self.Intefctyp],
        ['InterfaceId',self.InterfaceId],['HandlerContType',self.HandlerContType],['HandlerContId',self.HandlerContId],['LaserType',self.LaserType],['LaserId',self.LaserId],
        ['ExtraEQtype',self.ExtraEQtype],['ExtraEQId',self.ExtraEQId]]        
        for i in range(len(self.SDR_FIELD_LIST)): self.SDR_Rec_Summary[self.SDR_FIELD_LIST[i][0]].append(self.SDR_FIELD_LIST[i][1])
        return Starting_byte
    def PMR(self,Starting_byte):
        ''' Reads the PIN MAP record (PMR) from the stdf.'''
        UIndex,Starting_byte=self.U2(Starting_byte,1)#;print('Unique index associated with pin :',UIndex[0])
        ChanelType,Starting_byte=self.U2(Starting_byte,1)#;print('Channel Type :',ChanelType[0])
        ChanelName,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print('Channel Name :',ChanelName )
        PhNameOfPin,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print('Physical Name of Pin :',PhNameOfPin )
        LocalNameofPin,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print('Local name of Pin :',LocalNameofPin)
        HeadNumber,Starting_byte=self.U1(Starting_byte,1)#;print('Head number :',HeadNumber[0])
        SiteNumber,Starting_byte=self.U1(Starting_byte,1)#;print('Site number :',SiteNumber[0]);
        PMR_FIELD_LIST=[['File_Name',self.STDF_File.name],['UIndex',UIndex],['ChanelType',ChanelType],['ChanelName',ChanelName],['PhNameOfPin',PhNameOfPin],['LocalNameofPin',LocalNameofPin],['HeadNumber',HeadNumber],['SiteNumber',SiteNumber]]
        for i in range(len(PMR_FIELD_LIST)): self.PMR_Rec_Summary[PMR_FIELD_LIST[i][0]].append(PMR_FIELD_LIST[i][1])
        return Starting_byte
    def WCR(self,Starting_byte):
        ''' Reads the Wafer Configuration record (WCR) from the stdf.'''
        WaferSize,Starting_byte=self.R4(Starting_byte,1)#;print('Wafer Size :',WaferSize)
        DiHight,Starting_byte=self.R4(Starting_byte,1)#;print('Die Hight :',DiHight[0])
        DieWidht,Starting_byte=self.R4(Starting_byte,1)#;print('Die Width :',DieWidht[0])
        WaferUnits,Starting_byte=self.U1(Starting_byte,1)#;print('Wafer Units :',WaferUnits)
        Wflat,Starting_byte=self.C1(Starting_byte,1)#;print('Orientation of wafer flat :',Wflat)
        X_Co,Starting_byte=self.I2(Starting_byte,1)#;print('X Coordinate of Center Die of Wafer :',X_Co[0])
        Y_Co,Starting_byte=self.I2(Starting_byte,1)#;print('Y Coordinate of Center Die of Wafer :',Y_Co[0])
        POS_X,Starting_byte=self.C1(Starting_byte,1)#;print('Position of X direciton of Wafer :',X_Co)
        POS_Y,Starting_byte=self.C1(Starting_byte,1)#;print('Position of Y direction of wafer :',Y_Co);
        self.WCR_FIELD_LIST=[['File_Name',self.STDF_File.name],['WaferSize',WaferSize],['DiHight',DiHight],['DieWidht',DieWidht],['WaferUnits',WaferUnits],['Wflat',Wflat],['X_Co',X_Co],['Y_Co',Y_Co],['POS_X',POS_X],['POS_Y',POS_Y]]
        for i in range(len(self.WCR_FIELD_LIST)): self.WCR_Rec_Summary[self.WCR_FIELD_LIST[i][0]].append(self.WCR_FIELD_LIST[i][1])
        return Starting_byte
    def WIR(self,Starting_byte):
        ''' Reads the Wafer Infromation record (WIR) from the stdf.'''
        TestHeadnumber,Starting_byte=self.U1(Starting_byte,1)#;print("Test Head Number :",TestHeadnumber[0])
        SiteGourpNumber,Starting_byte=self.U1(Starting_byte,1)#;print('Site Group number :',SiteGourpNumber[0])
        DateEndTime,Starting_byte=self.U4(Starting_byte,1)#;print('Date and time first part tested :',DateEndTime[0])
        WfrId,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print('Local name of Pin :',WfrId[0]);
        self.WIR_FIELD_LIST=[['File_Name',self.STDF_File.name],['TestHeadnumber',TestHeadnumber],['SiteGourpNumber',SiteGourpNumber],['DateEndTime',DateEndTime],['WfrId',WfrId]]        
        for i in range(len(self.WIR_FIELD_LIST)): self.WIR_Rec_Summary[self.WIR_FIELD_LIST[i][0]].append(self.WIR_FIELD_LIST[i][1])
        return Starting_byte
    def PIR(self,Starting_byte):
        ''' Acts as a marker to indicate where testing of a particular part begins for each part tested by the test program. The PIR and the Part Results Record (PRR) bracket all the
            stored information pertaining to one tested part'''
        global Number_of_Tested_devices_per_instant_count
        TestHeadnumber,Starting_byte=self.U1(Starting_byte,1)#;print('Test Head number :',TestHeadnumber[0])
        TestSiteNumber,Starting_byte=self.U1(Starting_byte,1)#;print('Test Site Number :',TestSiteNumber[0])
        self.PIR_FIELD_LIST=[['TestHeadnumber',TestHeadnumber],['TestSiteNumber',TestSiteNumber]]       
        self.PIR_Rec_Summary['TestHeadnumber'].append(TestHeadnumber);self.PIR_Rec_Summary['TestSiteNumber'].append(TestSiteNumber);self.PIR_Rec_Summary["File_Name"].append(self.STDF_File.name)
        for i in range(0,20):   self.Temp_Rec_Summary[self.Full_FIELD_LIST[i]].append(self.MIR_Rec_Summary[self.Full_FIELD_LIST[i]][0])
        for i in range(20,22):  self.Temp_Rec_Summary[self.Full_FIELD_LIST[i]].append(self.PIR_FIELD_LIST[i-20][1])
        if self.Record_Details_list[1][self.Record_Number-1]!='PIR': Number_of_Tested_devices_per_instant_count=1
        elif self.Record_Details_list[1][self.Record_Number-1]=='PIR': Number_of_Tested_devices_per_instant_count+=1        
        return Starting_byte
    def PTR(self,Starting_byte):
        '''Reads the Parametric Test Result Record (PTR) from the STDF.
           This is one of the most used and useful record in the stdf.  All the devices Parametric data will be stored in this record.
           TestNumber, TestName,Site,TestFlag ETC....'''        
        TestNumber,Starting_byte=self.U4(Starting_byte,1)#;print('Test number :',TestNumber)
        TestHeadNumber,Starting_byte=self.U1(Starting_byte,1)#;print('Test Head Number :',TestHeadNumber)
        SiteNumber,Starting_byte=self.U1(Starting_byte,1)#;print('Site Number :',SiteNumber)
        TestFlag,Starting_byte=self.B1(Starting_byte,1)#;print('Test flag :',TestFlag)
        ParamFlag,Starting_byte=self.B1(Starting_byte,1)#;print('Parametric flag :',ParamFlag)
        TestResult,Starting_byte=self.R4(Starting_byte,1)#;print('Test result :',TestResult)
        TestName,Starting_byte=self.Missing_Invalid_Data(Starting_byte,TestNumber,self.PTR_Rec_Summary,'Test_Txt')
        AlaramName,Starting_byte=self.Missing_Invalid_Data(Starting_byte,TestNumber,self.PTR_Rec_Summary,'Alaram_Id')#;print('Alaram name :',AlaramName)
        if str(TestNumber)+";"+TestName not in self.TestNumbers and Starting_byte<self.End_Record_Byte:
            OptFlag,Starting_byte=self.B1(Starting_byte,1)#;print('Optional Data Flag :',OptFlag)
            TRSE,Starting_byte=self.I1(Starting_byte,1) #if OptFlag[7:8]!='1' else (None,Starting_byte)#;print('Test Result Scaling exponent :',TRSE)
            LLSE,Starting_byte=self.I1(Starting_byte,1) #if (OptFlag[3:4]!='1' or OptFlag[1:2]!='1') else (None,Starting_byte)#;print('Low limit scaling exponent :',LLSE)
            HLSE,Starting_byte=self.I1(Starting_byte,1) #if (OptFlag[2:3]!='1' or OptFlag[0:1]!='1') else (None,Starting_byte)#;print('High limit scaling exponent :',HLSE)
            LowLim,Starting_byte=self.R4(Starting_byte,1) #if (OptFlag[3:4]!='1' or OptFlag[1:2]!='1') else (None,Starting_byte)#;print('Low Limit :',LowLim)
            HighLim,Starting_byte=self.R4(Starting_byte,1) #if (OptFlag[2:3]!='1' or OptFlag[0:1]!='1') else (None,Starting_byte)
            TestUnit,Starting_byte=self.Missing_Invalid_Data(Starting_byte,TestNumber,self.PTR_Rec_Summary,'Units')#;print('Test Units :',TestUnit)
            CRFS,Starting_byte=self.Missing_Invalid_Data(Starting_byte,TestNumber,self.PTR_Rec_Summary,'C_RESFMT')#;print('C result Fmt string :',CRFS)
            CLLFS,Starting_byte=self.Missing_Invalid_Data(Starting_byte,TestNumber,self.PTR_Rec_Summary,'C_LLMFMT')#;print('C Low lim Fmt string:',CLLFS)
            CHLFS,Starting_byte=self.Missing_Invalid_Data(Starting_byte,TestNumber,self.PTR_Rec_Summary,'C_HLMFMT')#;print('C High Lim Fmt string :',CHLFS)            
            LowSpec,Starting_byte=self.R4(Starting_byte,1) #if OptFlag[5:6]!='1' else ('',Starting_byte)
            HighSpec,Starting_byte=self.R4(Starting_byte,1) #if OptFlag[4:5]!='1' else ('',Starting_byte)            
        elif str(TestNumber)+";"+TestName not in self.TestNumbers and Starting_byte==self.End_Record_Byte:
            OptFlag,Starting_byte=0, Starting_byte#;print('Optional Data Flag :',OptFlag)
            TRSE,Starting_byte=0, Starting_byte#;print('Test Result Scaling exponent :',TRSE)
            LLSE,Starting_byte=0, Starting_byte#;print('Low limit scaling exponent :',LLSE)
            HLSE,Starting_byte=0, Starting_byte#;print('High limit scaling exponent :',HLSE)
            LowLim,Starting_byte=0.0, Starting_byte#;print('Low Limit :',LowLim)
            HighLim,Starting_byte=0.0, Starting_byte#;print('High limit :',HighLim)
            TestUnit,Starting_byte='', Starting_byte#;print('Test Units :',TestUnit)
            CRFS,Starting_byte='', Starting_byte#;print('C result Fmt string :',CRFS)
            CLLFS,Starting_byte='', Starting_byte#;print('C Low lim Fmt string:',CLLFS)
            CHLFS,Starting_byte='', Starting_byte#;print('C High Lim Fmt string :',CHLFS)
            LowSpec,Starting_byte=0.0, Starting_byte#;print('Low Spec Value :',LowSpec)
            HighSpec,Starting_byte=0.0, Starting_byte#;print('High Spec value :',HighSpec)
        elif str(TestNumber)+";"+TestName in self.TestNumbers:
            OptFlag=self.PTR_Rec_Summary['Opt_flag'][self.PTR_Rec_Summary['TestNumber'].index(TestNumber)]#;print('Optional Data Flag :',OptFlag)
            TRSE=self.PTR_Rec_Summary['Res_Scal'][self.PTR_Rec_Summary['TestNumber'].index(TestNumber)]#;print('Test Result Scaling exponent :',TRSE)
            LLSE=self.PTR_Rec_Summary['Llm_Scal'][self.PTR_Rec_Summary['TestNumber'].index(TestNumber)]#;print('Low limit scaling exponent :',LLSE)
            HLSE=self.PTR_Rec_Summary['Hlm_Scal'][self.PTR_Rec_Summary['TestNumber'].index(TestNumber)]#;print('High limit scaling exponent :',HLSE)
            LowLim=self.PTR_Rec_Summary['Lo_limit'][self.PTR_Rec_Summary['TestNumber'].index(TestNumber)]#;print('Low Limit :',LowLim)
            HighLim=self.PTR_Rec_Summary['Hi_limit'][self.PTR_Rec_Summary['TestNumber'].index(TestNumber)]#;print('High limit :',HighLim)
            TestUnit=self.PTR_Rec_Summary['Units'][self.PTR_Rec_Summary['TestNumber'].index(TestNumber)]#;print('Test Units :',TestUnit)
            CRFS=self.PTR_Rec_Summary['C_RESFMT'][self.PTR_Rec_Summary['TestNumber'].index(TestNumber)]#;print('C result Fmt string :',CRFS)
            CLLFS=self.PTR_Rec_Summary['c_LLMFMT'][self.PTR_Rec_Summary['TestNumber'].index(TestNumber)]#;print('C Low lim Fmt string:',CLLFS)
            CHLFS=self.PTR_Rec_Summary['C_HLMFMT'][self.PTR_Rec_Summary['TestNumber'].index(TestNumber)]#;print('C High Lim Fmt string :',CHLFS)
            LowSpec=self.PTR_Rec_Summary['LO_SPEC'][self.PTR_Rec_Summary['TestNumber'].index(TestNumber)]#;print('Low Spec Value :',LowSpec)
            HighSpec=self.PTR_Rec_Summary['HI_SPEC'][self.PTR_Rec_Summary['TestNumber'].index(TestNumber)]#;print('High Spec value :',HighSpec)
        
        if LowLim!=None and LLSE!=None: LowLim=LowLim *(10**LLSE)
        if HighLim!=None and HLSE!=None: HighLim=HighLim*(10**HLSE)
        if TestResult!=None and TRSE!='': TestResult=TestResult*(10**TRSE)
        if CLLFS!=None and CLLFS!='': LowLim=round(LowLim,int(CLLFS.split('.')[1].split('f')[0]))
        if CHLFS!=None and CHLFS!='': HighLim=round(HighLim,int(CHLFS.split('.')[1].split('f')[0]))
        if TestUnit!=None and TestUnit!='': TestUnit=self.Scale_values[TRSE][0]+str(TestUnit)
        ## TestFlag_Info
        Alarm_Detected_during_testing= True if TestFlag[7:8]=='1' else False# Bit0
        Test_result_is_valid= True if TestFlag[6:7]=='0' else False#Bit1
        Test_result_is_reliable= True if TestFlag[5:6]=='0' else False#Bit2
        Time_out_occured= True if TestFlag[4:5]=='1' else False#Bit3
        Test_exicuted= True if TestFlag[3:4]=='0' else False#Bit4
        Test_aborted= True if TestFlag[2:3]=='1' else False#Bit5
        Test_passed = (True if TestFlag[0:1]=='0' else False) if TestFlag[1:2]=='0' else 'Invalid'#Bit6,7
        ##PARM_FLAG_INFO
        Scale_Error= True if ParamFlag[7:8]=='1' else False# Bit0
        Drift_Error= True if ParamFlag[6:7]=='1' else False# Bit1
        Oscillation_detected= True if ParamFlag[5:6]=='1' else False# Bit2
        Measured_value_Higher_than_High_test_limit= True if ParamFlag[4:5]=='1' else False# Bit3
        Measured_value_Lower_than_Low_test_limit=  True if ParamFlag[3:4]=='1' else False# Bit4
        Test_Pass_Fail= 'Pass or Fail with Standerd limits' if ParamFlag[2:3]=='0' else 'Pass with alternate limits'# Bit5
        Failed_at_low_lim= True if ParamFlag[1:2]=='0' else False# Bit6
        Failed_at_high_lim = True if ParamFlag[0:1]=='0' else False# Bit7
        #Result
        #if TestFlag[2:8]!='000000' and ParamFlag[5:8]!='000': TestResult=None        
        #if TestResult!=None and TRSE!=None: TestResult=TestResult*(10**self.Scale_values[TRSE][2])
        
        # OPT FLAG
        '''TRSE,Starting_byte=self.I1(Starting_byte,1) if OptFlag[7:8]!='1' else (None,Starting_byte)#;print('Test Result Scaling exponent :',TRSE)
        LLSE,Starting_byte=self.I1(Starting_byte,1) if (OptFlag[3:4]!='1' or OptFlag[1:2]!='1') else (None,Starting_byte)#;print('Low limit scaling exponent :',LLSE)
        HLSE,Starting_byte=self.I1(Starting_byte,1) if (OptFlag[2:3]!='1' or OptFlag[0:1]!='1') else (None,Starting_byte)#;print('High limit scaling exponent :',HLSE)
        LowLim,Starting_byte=self.R4(Starting_byte,1) if (OptFlag[3:4]!='1' or OptFlag[1:2]!='1') else (None,Starting_byte)#;print('Low Limit :',LowLim)
        HighLim,Starting_byte=self.R4(Starting_byte,1) if (OptFlag[2:3]!='1' or OptFlag[0:1]!='1') else (None,Starting_byte)
        LowSpec,Starting_byte=self.R4(Starting_byte,1) if OptFlag[5:6]!='1' else ('',Starting_byte)
        HighSpec,Starting_byte=self.R4(Starting_byte,1) if OptFlag[4:5]!='1' else ('',Starting_byte)'''

        if str(TestNumber)+";"+TestName not in self.TestNumbers:
            self.TestNumbers[str(TestNumber)+";"+TestName]= self.Record_Number
            self.Test_Limit_Details[str(TestNumber)+";"+TestName]=[LowLim,HighLim,TestUnit]
            self.Full_Rec_Summary[str(TestNumber)+";"+TestName]=[]
            self.Full_FIELD_LIST.append(str(TestNumber)+";"+TestName)
            self.Temp_Rec_Summary[str(TestNumber)+";"+TestName]=[]
            Dummy_list=[]
            if len(self.Full_Rec_Summary['File_Name'])>=1:
                for i in range(len(self.Full_Rec_Summary['File_Name'])) : Dummy_list.append(nan)
                self.Full_Rec_Summary[str(TestNumber)+";"+TestName].extend(Dummy_list)
                Dummy_list=[]
            for i in range(Number_of_Tested_devices_per_instant_count) : Dummy_list.append(nan)
            self.Temp_Rec_Summary[str(TestNumber)+";"+TestName].extend(Dummy_list)
        elif self.Lists_in_Temp_Rec_Summary_are_empty==True and str(TestNumber)+";"+TestName in self.TestNumbers:
            Dummy_list=[]
            for i in range(Number_of_Tested_devices_per_instant_count) : Dummy_list.append(nan)
            for j in range(self.Full_FIELD_LIST.index('PartFix')+1,len(self.Full_FIELD_LIST)): self.Temp_Rec_Summary[self.Full_FIELD_LIST[j]].extend(Dummy_list)
            self.Lists_in_Temp_Rec_Summary_are_empty=False 
        self.PTR_Field_List=[['File_Name',self.STDF_File.name],['Record_number',self.Record_Number],['TestNumber',TestNumber],['TestHeadNumber',TestHeadNumber],['TestSiteNumber',SiteNumber],
        ['TestFlag',TestFlag],['Paramatric_flag',ParamFlag],['Result',TestResult],['Test_Txt',TestName],['Alaram_Id',AlaramName],['Opt_flag',OptFlag],['Res_Scal',TRSE],
        ['Llm_Scal',LLSE],['Hlm_Scal',HLSE],['Lo_limit',LowLim],['Hi_limit',HighLim],['Units',TestUnit],['C_RESFMT',CRFS], ['c_LLMFMT',CLLFS],['C_HLMFMT',CHLFS],['LO_SPEC',LowSpec],['HI_SPEC',HighSpec],
        ['Alarm_Detected_during_testing',Alarm_Detected_during_testing],['Test_result_is_valid',Test_result_is_valid],['Test_result_is_reliable',Test_result_is_reliable],['Time_out_occured',Time_out_occured]
        ,['Test_exicuted',Test_exicuted],['Test_aborted',Test_aborted],['Test_passed',Test_passed],['Scale_Error',Scale_Error],['Drift_Error',Drift_Error]
        ,['Oscillation_detected',Oscillation_detected],['Measured_value_Higher_than_High_test_limit',Measured_value_Higher_than_High_test_limit],['Measured_value_Lower_than_Low_test_limit',Measured_value_Lower_than_Low_test_limit]
        ,['Test_Pass_Fail',Test_Pass_Fail],['Failed_at_low_lim',Failed_at_low_lim],['Failed_at_high_lim',Failed_at_high_lim]]            
        for i in range(len(self.PTR_Field_List)): self.PTR_Rec_Summary[self.PTR_Field_List[i][0]].append(self.PTR_Field_List[i][1])            
        for i in range(Number_of_Tested_devices_per_instant_count):
            if len(self.Temp_Rec_Summary[str(TestNumber)+";"+TestName])<=len(self.Temp_Rec_Summary['File_Name']) and self.Temp_Rec_Summary['TestHeadnumber'][i]==TestHeadNumber and self.Temp_Rec_Summary['TestSiteNumber'][i]==SiteNumber and self.Temp_Rec_Summary[str(TestNumber)+";"+TestName][i] is nan: self.Temp_Rec_Summary[str(TestNumber)+";"+TestName][i]=TestResult; break                                   
        
        return Starting_byte
    def MPR(self,Starting_byte):
        ''' Reads the Multiple Parametric Record (MPR) from STDF file.
            Similar to PTR MPR record will give you the Multiple parameter data in encrypted in the STDF.'''
        TestNumber,Starting_byte=self.U4(Starting_byte,1)#;print('Test Number:',TestNumber)
        TestHeadNumber,Starting_byte=self.U1(Starting_byte,1)#;print('Head number:',TestHeadNumber)
        SiteNumber,Starting_byte=self.U1(Starting_byte,1)#;print('Site Number:',SiteNumber)
        TestFlag,Starting_byte=self.B1(Starting_byte,1)#;print('Test flag:',TestFlag)
        ParamFlag,Starting_byte=self.B1(Starting_byte,1)#;print('Parm flag:',ParamFlag)
        Rtn_Icnt,Starting_byte=self.Zero_len_byte(Starting_byte,self.U2) #;print('count of J:',Rtn_Icnt)
        Rslt_cnt,Starting_byte=self.Zero_len_byte(Starting_byte,self.U2)#;print('count of k',Rslt_cnt)
        
        if (Rtn_Icnt==1 and Rtn_Icnt!=0): Rtn_Stat,Starting_byte=self.N1(Starting_byte,1);Rtn_Stat_str =str(Rtn_Stat)
        elif (Rtn_Icnt!='' and Rtn_Icnt>1):
            Rtn_Stat=[]
            for i in range(0,Rtn_Icnt): Array_val,Starting_byte=self.N1(Starting_byte,1);Rtn_Stat.append(Array_val)
            Rtn_Stat_str = ','.join(str(e) for e in Rtn_Stat)
        elif Rtn_Icnt=='':
            Rtn_Stat_str =''
            Rtn_Stat=['']
        if (Rslt_cnt==1 and Rslt_cnt!=0): TestResult,Starting_byte=self.R4(Starting_byte,1);TestResult=[(TestResult)]
        elif (Rslt_cnt!="" and Rslt_cnt>1):
            TestResult=[]
            for i in range(0,Rslt_cnt): Array_val,Starting_byte=self.R4(Starting_byte,1);TestResult.append(Array_val)
            #TestResult_str=','.join(str(e) for e in TestResult)
        TestName,Starting_byte=self.Missing_Invalid_Data(Starting_byte,TestNumber,self.MPR_Rec_Summary,'TestName')#;print('Test Lbl:',TestName)
        AlaramName,Starting_byte=self.Missing_Invalid_Data(Starting_byte,TestNumber,self.MPR_Rec_Summary,'AlaramName')#;print('Name of alaram:',AlaramName)
        #Corresponding data:
        if TestNumber not in self.TestNumbers and Starting_byte<self.End_Record_Byte:
            OptFlag,Starting_byte=self.B1(Starting_byte,1)#;print('OPT_FLAG',OptFlag)
            TRSE,Starting_byte=self.I1(Starting_byte,1) #if OptFlag[7:8]!='1' else (None,Starting_byte)#;print('Test Result Scaling exponent :',TRSE)
            LLSE,Starting_byte=self.I1(Starting_byte,1) #if (OptFlag[3:4]!='1' or OptFlag[1:2]!='1') else (None,Starting_byte)#;print('Low limit scaling exponent :',LLSE)
            HLSE,Starting_byte=self.I1(Starting_byte,1) #if (OptFlag[2:3]!='1' or OptFlag[0:1]!='1') else (None,Starting_byte)#;print('High limit scaling exponent :',HLSE)
            LowLim,Starting_byte=self.R4(Starting_byte,1) #if (OptFlag[3:4]!='1' or OptFlag[1:2]!='1') else (None,Starting_byte)#;print('Low Limit :',LowLim)
            HighLim,Starting_byte=self.R4(Starting_byte,1) #if (OptFlag[2:3]!='1' or OptFlag[0:1]!='1') else (None,Starting_byte)
            Start_in,Starting_byte=self.R4(Starting_byte,1)#;print('Start_in:',Start_in)
            Incr_in,Starting_byte=self.R4(Starting_byte,1)#;print('Incr_in:',Incr_in)            
            if (Rtn_Icnt==1 and Rtn_Icnt!=0): Rtn_indx,Starting_byte=self.U2(Starting_byte,1);Rtn_indx_str=str(Rtn_indx);Rtn_indx=[str(Rtn_indx)]
            elif (Rtn_Icnt!='' and Rtn_Icnt>1):
                Rtn_indx=[]
                for i in range(0,Rtn_Icnt): Array_val,Starting_byte=self.U2(Starting_byte,1);Rtn_indx.append(Array_val)
                Rtn_indx_str= ','.join(str(e) for e in Rtn_indx)
            elif (Rtn_Icnt==0 or Rtn_Icnt==""):
                Rtn_indx=[]
                Rtn_indx_str= ','.join(str(e) for e in Rtn_indx)
            TestUnit,Starting_byte=self.Missing_Invalid_Data(Starting_byte,TestNumber,self.MPR_Rec_Summary,'TestUnit')#;print('Units',TestUnit)
            Units_in,Starting_byte=self.Missing_Invalid_Data(Starting_byte,TestNumber,self.MPR_Rec_Summary,'Units_in')#;print('Unitsin',Units_in)
            CRFS,Starting_byte=self.Missing_Invalid_Data(Starting_byte,TestNumber,self.MPR_Rec_Summary,'CRFS')#;print('C_Resfmt',CRFS)
            CLLFS,Starting_byte=self.Missing_Invalid_Data(Starting_byte,TestNumber,self.MPR_Rec_Summary,'CLLFS')#;print('C_llmfmt',CLLFS)
            CHLFS,Starting_byte=self.Missing_Invalid_Data(Starting_byte,TestNumber,self.MPR_Rec_Summary,'CHLFS')#;print('C_Hlmfmt',CHLFS)
            LowSpec,Starting_byte=self.R4(Starting_byte,1) #if OptFlag[5:6]!='1' else ('',Starting_byte)
            HighSpec,Starting_byte=self.R4(Starting_byte,1) #if OptFlag[4:5]!='1' else ('',Starting_byte)
            
        elif TestNumber not in self.TestNumbers and Starting_byte==self.End_Record_Byte:
            OptFlag=''#;print('OPT_FLAG',OptFlag)
            TRSE=''#;print('RES_SCAL',TRSE)
            LLSE=''#;print('LLM_SCAL',LLSE)
            HLSE=''#;print('Hlm Scal',HLSE)
            LowLim=''#;print('Lo lim',LowLim)
            HighLim=''#;print('Hi lim',HighLim)
            Start_in=''#;print('Start_in:',Start_in)
            Incr_in=''#;print('Incr_in:',Incr_in)            
            if (Rtn_Icnt==1 and Rtn_Icnt!=0): Rtn_indx,Starting_byte=self.U2(Starting_byte,1);Rtn_indx_str=str(Rtn_indx);Rtn_indx=[str(Rtn_indx)]
            elif (Rtn_Icnt!="" and Rtn_Icnt>1):
                Rtn_indx=[]
                for i in range(0,Rtn_Icnt): Array_val,Starting_byte=self.U2(Starting_byte,1);Rtn_indx.append(Array_val)
                Rtn_indx_str= ','.join(str(e) for e in Rtn_indx)
            elif Rtn_Icnt==0 or Rtn_Icnt=="":
                Rtn_indx=[]
                Rtn_indx_str= ','.join(str(e) for e in Rtn_indx)
            TestUnit=''#;print('Units',TestUnit)
            Units_in=''#;print('Unitsin',Units_in)
            CRFS=''#;print('C_Resfmt',CRFS)
            CLLFS=''#;print('C_llmfmt',CLLFS)
            CHLFS=''#;print('C_Hlmfmt',CHLFS)
            LowSpec=''#;print('Lo_spec',LowSpec)
            HighSpec=''#;print('Hi_spec',HighSpec)
        elif TestNumber in self.TestNumbers:
            OptFlag=self.MPR_Rec_Summary['OptFlag'][self.MPR_Rec_Summary['TestNumber'].index(TestNumber)]#;print('Optional Data Flag :',OptFlag)
            TRSE=self.MPR_Rec_Summary['TRSE'][self.MPR_Rec_Summary['TestNumber'].index(TestNumber)]#;print('Test Result Scaling exponent :',TRSE)
            LLSE=self.MPR_Rec_Summary['LLSE'][self.MPR_Rec_Summary['TestNumber'].index(TestNumber)]#;print('Low limit scaling exponent :',LLSE)
            HLSE=self.MPR_Rec_Summary['HLSE'][self.MPR_Rec_Summary['TestNumber'].index(TestNumber)]#;print('High limit scaling exponent :',HLSE)
            LowLim=self.MPR_Rec_Summary['LowLim'][self.MPR_Rec_Summary['TestNumber'].index(TestNumber)]#;print('Low Limit :',LowLim)
            HighLim=self.MPR_Rec_Summary['HighLim'][self.MPR_Rec_Summary['TestNumber'].index(TestNumber)]#;print('High limit :',HighLim)
            Start_in=self.MPR_Rec_Summary['Start_in'][self.MPR_Rec_Summary['TestNumber'].index(TestNumber)]
            Incr_in=self.MPR_Rec_Summary['Incr_in'][self.MPR_Rec_Summary['TestNumber'].index(TestNumber)]
            Rtn_indx_str=self.MPR_Rec_Summary['Rtn_indx_str'][self.MPR_Rec_Summary['TestNumber'].index(TestNumber)]
            Rtn_indx=Rtn_indx_str.split(",")
            TestUnit=self.MPR_Rec_Summary['TestUnit'][self.MPR_Rec_Summary['TestNumber'].index(TestNumber)]
            Units_in=self.MPR_Rec_Summary['Units_in'][self.MPR_Rec_Summary['TestNumber'].index(TestNumber)]
            CRFS=self.MPR_Rec_Summary['CRFS'][self.MPR_Rec_Summary['TestNumber'].index(TestNumber)]
            CLLFS=self.MPR_Rec_Summary['CLLFS'][self.MPR_Rec_Summary['TestNumber'].index(TestNumber)]
            CHLFS=self.MPR_Rec_Summary['CHLFS'][self.MPR_Rec_Summary['TestNumber'].index(TestNumber)]
            LowSpec=self.MPR_Rec_Summary['LowSpec'][self.MPR_Rec_Summary['TestNumber'].index(TestNumber)]
            HighSpec=self.MPR_Rec_Summary['HighSpec'][self.MPR_Rec_Summary['TestNumber'].index(TestNumber)]
        
        if LowLim!=None and LLSE!=None: LowLim=LowLim *(10**LLSE)
        if HighLim!=None and HLSE!=None: HighLim=HighLim*(10**HLSE)
        if TestResult!=None and TRSE!='': TestResult=[i*(10**TRSE) for i in TestResult]
        if CLLFS!=None and CLLFS!='': LowLim=round(LowLim,int(CLLFS.split('.')[1].split('f')[0]))
        if CHLFS!=None and CHLFS!='': HighLim=round(HighLim,int(CHLFS.split('.')[1].split('f')[0]))
        if TestUnit!=None and TestUnit!='': TestUnit=self.Scale_values[TRSE][0]+str(TestUnit)
        ## TestFlag_Info
        Alarm_Detected_during_testing= True if TestFlag[7:8]=='1' else False# Bit0
        #Test_result_is_valid= True if TestFlag[6:7]=='0' else False#Bit1
        Test_result_is_reliable= True if TestFlag[5:6]=='0' else False#Bit2
        Time_out_occured= True if TestFlag[4:5]=='1' else False#Bit3
        Test_exicuted= True if TestFlag[3:4]=='0' else False#Bit4
        Test_aborted= True if TestFlag[2:3]=='1' else False#Bit5
        Test_passed = (True if TestFlag[0:1]=='0' else False) if TestFlag[1:2]=='0' else 'Invalid'#Bit6,7
        ##PARM_FLAG_INFO
        Scale_Error= True if ParamFlag[7:8]=='1' else False# Bit0
        Drift_Error= True if ParamFlag[6:7]=='1' else False# Bit1
        Oscillation_detected= True if ParamFlag[5:6]=='1' else False# Bit2
        Measured_value_Higher_than_High_test_limit= True if ParamFlag[4:5]=='1' else False# Bit3
        Measured_value_Lower_than_Low_test_limit=  True if ParamFlag[3:4]=='1' else False# Bit4
        Test_Pass_Fail= 'Pass or Fail with Standerd limits' if ParamFlag[2:3]=='0' else 'Pass with alternate limits'# Bit5
        Failed_at_low_lim= True if ParamFlag[1:2]=='0' else False# Bit6
        Failed_at_high_lim = True if ParamFlag[0:1]=='0' else False# Bit7
        if TestNumber not in self.TestNumbers:
            self.TestNumbers[TestNumber]= self.Record_Number
            for i in range(0, len(Rtn_indx)):
                TestName1=TestName+'_'+(self.PMR_Rec_Summary['ChanelName'][self.PMR_Rec_Summary['UIndex'].index(int(Rtn_indx[i]))])
                self.Full_Rec_Summary[str(TestNumber)+";"+TestName1]=[]
                self.Full_FIELD_LIST.append(str(TestNumber)+";"+TestName1)
                self.Temp_Rec_Summary[str(TestNumber)+";"+TestName1]=[]                
                self.Test_Limit_Details[str(TestNumber)+";"+TestName1]=[LowLim,HighLim,TestUnit]
                Dummy_list=[]
                if len(self.Full_Rec_Summary['File_Name'])>=1:
                    for i in range(len(self.Full_Rec_Summary['File_Name'])) : Dummy_list.append(nan)
                    self.Full_Rec_Summary[str(TestNumber)+";"+TestName1].extend(Dummy_list)
                    Dummy_list=[]
                for i in range(Number_of_Tested_devices_per_instant_count) : Dummy_list.append(nan)
                self.Temp_Rec_Summary[str(TestNumber)+";"+TestName1].extend(Dummy_list)
        elif self.Lists_in_Temp_Rec_Summary_are_empty==True and TestNumber in self.TestNumbers:
            Dummy_list=[]
            for i in range(Number_of_Tested_devices_per_instant_count) : Dummy_list.append(nan)
            for j in range(self.Full_FIELD_LIST.index('PartFix')+1,len(self.Full_FIELD_LIST)): self.Temp_Rec_Summary[self.Full_FIELD_LIST[j]].extend(Dummy_list)        
            self.Lists_in_Temp_Rec_Summary_are_empty=False
        for i in range(0, len(Rtn_indx)):
            TestName1=TestName+'_'+(self.PMR_Rec_Summary['ChanelName'][self.PMR_Rec_Summary['UIndex'].index(int(Rtn_indx[i]))])            
            self.MPR_Field_List=[['File_Name',self.STDF_File.name],['Record_number',self.Record_Number],['TestNumber',TestNumber],['TestHeadNumber',TestHeadNumber],['SiteNumber',SiteNumber],['TestFlag',TestFlag],['ParamFlag',ParamFlag],['Rtn_Icnt',Rtn_Icnt],
            ['Rslt_cnt',Rslt_cnt],['Rtn_Stat_str',Rtn_Stat_str],['TestResult_str',TestResult[i]],['TestName',TestName1],['AlaramName',AlaramName],['OptFlag',OptFlag],['TRSE',TRSE],['LLSE',LLSE],['HLSE',HLSE],['LowLim',LowLim],['HighLim',HighLim],['Start_in',Start_in],
            ['Incr_in',Incr_in],['Rtn_indx_str',Rtn_indx_str],['TestUnit',TestUnit],['Units_in',Units_in],['CRFS',CRFS],['CLLFS',CLLFS],['CHLFS',CHLFS],['LowSpec',LowSpec],['HighSpec',HighSpec],['Alarm_Detected_during_testing',Alarm_Detected_during_testing],
            ['Test_result_is_reliable',Test_result_is_reliable],['Time_out_occured',Time_out_occured],['Test_exicuted',Test_exicuted],['Test_aborted',Test_aborted],['Test_passed',Test_passed],['Scale_Error',Scale_Error],['Drift_Error',Drift_Error]
            ,['Oscillation_detected',Oscillation_detected],['Measured_value_Higher_than_High_test_limit',Measured_value_Higher_than_High_test_limit],['Measured_value_Lower_than_Low_test_limit',Measured_value_Lower_than_Low_test_limit]
            ,['Test_Pass_Fail',Test_Pass_Fail],['Failed_at_low_lim',Failed_at_low_lim],['Failed_at_high_lim',Failed_at_high_lim]]
            for j in range(len(self.MPR_Field_List)): self.MPR_Rec_Summary[self.MPR_Field_List[j][0]].append(self.MPR_Field_List[j][1])
            for k in range(Number_of_Tested_devices_per_instant_count):
                if len(self.Temp_Rec_Summary[str(TestNumber)+";"+TestName1])<=len(self.Temp_Rec_Summary['File_Name']) and self.Temp_Rec_Summary['TestHeadnumber'][k]==TestHeadNumber and self.Temp_Rec_Summary['TestSiteNumber'][k]==SiteNumber and self.Temp_Rec_Summary[str(TestNumber)+";"+TestName1][k] is nan: self.Temp_Rec_Summary[str(TestNumber)+";"+TestName1][k]=TestResult[i];break
        return Starting_byte
    def FTR(self,Starting_byte):
        ''' Reads the Functional Test record (FTR) from the STDF.
            Unlike PTR & MPR , FTR will reads the fucntional tests in the stdf, and tells the wether the test is pass or fail.'''    
        TestNumber,Starting_byte=self.U4(Starting_byte,1)#;print('TestNumber :',TestNumber[0])
        TestHeadNumber,Starting_byte=self.U1(Starting_byte,1)#;print('Test Head Number :',TestHeadNumber[0])
        SiteNumber,Starting_byte=self.U1(Starting_byte,1)#;print('Site Number :',SiteNumber[0])        
        TestFlag,Starting_byte=self.B1(Starting_byte,1)#;print('Test Flag :',TestFlag[0])
        TestResult='P' if TestFlag=='00000000' else 'F'
        if  Starting_byte<self.End_Record_Byte:
            OptFlag,Starting_byte=self.B1(Starting_byte,1)#;print('Optional Flag :',OptFlag[0])
            Cycl_Cnt,Starting_byte=self.U4(Starting_byte,1) #if OptFlag[7:8]!='1' else (None, Starting_byte) #;print('Vector Cycle count :',Cycl_Cnt[0])
            Rel_V_Addr,Starting_byte=self.U4(Starting_byte,1) #if OptFlag[6:7]!='1' else (None, Starting_byte)#;print('Relative vector address :',Rel_V_Addr[0])
            Rept_C_Vctr,Starting_byte=self.U4(Starting_byte,1)#if OptFlag[5:6]!='1' else (None, Starting_byte)#;print('Vector Repeat count :',Rept_C_Vctr[0])
            Num_P_Fail,Starting_byte=self.U4(Starting_byte,1)#if OptFlag[4:5]!='1' else (None, Starting_byte)#;print('Pin count with 1 or more Failures',Num_P_Fail[0])
            X_Fail_Adrs,Starting_byte=self.I4(Starting_byte,1)#if OptFlag[3:4]!='1' else (None, Starting_byte)#;print('X Logical dev Fail address :',X_Fail_Adrs[0])
            Y_Fail_Adrs,Starting_byte=self.I4(Starting_byte,1)#if OptFlag[3:4]!='1' else (None, Starting_byte)#;print('Y Logical dev Fail address :',Y_Fail_Adrs[0])
            Vect_offset,Starting_byte=self.I2(Starting_byte,1)#if OptFlag[2:3]!='1' else (None, Starting_byte)#;print('Offset from vector of intrest :',Vect_offset[0])
            Rtn_PmrIndex_cnt,Starting_byte= self.U2(Starting_byte,1) if Starting_byte < self.End_Record_Byte else ('', Starting_byte)
            Pgm_StateIndex,Starting_byte= self.U2(Starting_byte,1) if Starting_byte < self.End_Record_Byte else('', Starting_byte)
            if (Rtn_PmrIndex_cnt==1 and Rtn_PmrIndex_cnt!=0): RTN_Index_ary,Starting_byte=self.U2(Starting_byte,1);RTN_State_ary,Starting_byte=self.U2(Starting_byte,1)
            elif Rtn_PmrIndex_cnt!="" and Rtn_PmrIndex_cnt>1:
                RTN_Index_ary=[]
                RTN_State_ary=[]
                for i in range(0,Rtn_PmrIndex_cnt): Array_val,Starting_byte=self.U2(Starting_byte,1);RTN_Index_ary.append(Array_val)
                for i in range(0,Rtn_PmrIndex_cnt): Array_val,Starting_byte=self.U2(Starting_byte,1);RTN_State_ary.append(Array_val)
            elif Rtn_PmrIndex_cnt==0 or Rtn_PmrIndex_cnt=="":
                RTN_Index_ary=[]
                RTN_State_ary=[]
            RTN_Index_ary_str=','.join(str(e) for e in RTN_Index_ary)
            RTN_State_ary_str=','.join(str(e) for e in RTN_State_ary)
            if (Pgm_StateIndex==1 and Pgm_StateIndex!=0): Pgm_State_indx_ary,Starting_byte=self.U2(Starting_byte,1);Pgm_State_indx_ary_str=Pgm_State_indx_ary;Pgm_State_ary,Starting_byte=self.U2(Starting_byte,1);Pgm_State_ary_str=Pgm_State_ary
            elif Pgm_StateIndex!="" and Pgm_StateIndex>1:
                Pgm_State_indx_ary=[]
                Pgm_State_ary=[]
                for i in range(0,Pgm_StateIndex): Array_val,Starting_byte=self.U2(Starting_byte,1);Pgm_State_indx_ary.append(Array_val)
                for i in range(0,Pgm_StateIndex): Array_val,Starting_byte=self.U2(Starting_byte,1);Pgm_State_ary.append(Array_val)
            elif Pgm_StateIndex==0 or  Pgm_StateIndex=="":
                Pgm_State_indx_ary=[]
                Pgm_State_ary=[]
            Pgm_State_indx_ary_str=','.join(str(e) for e in Pgm_State_indx_ary)
            Pgm_State_ary_str=','.join(str(e) for e in Pgm_State_ary)
            #Failpin,Starting_byte= self.DN(Starting_byte,1) if Starting_byte < self.End_Record_Byte else '', Starting_byte #;print('Fail pin bit field :',Failpin,Starting_byte)
            Failpin,Starting_byte= self.DN(Starting_byte,1) if Starting_byte < self.End_Record_Byte else ('', Starting_byte)          
            VectNum,Starting_byte=self.Missing_Invalid_Data(Starting_byte,TestNumber,self.FTR_Rec_Summary,'VectNum')#;print('Vect Module pattern name :',VectNum)
            Timesetname,Starting_byte=self.Missing_Invalid_Data(Starting_byte,TestNumber,self.FTR_Rec_Summary,'Timesetname')#;print('Time set name :',Timesetname)#[0].decode('utf-8'))
            opcode,Starting_byte=self.Missing_Invalid_Data(Starting_byte,TestNumber,self.FTR_Rec_Summary,'opcode')#;print('Vector Op code :',opcode)
            Test_Txt,Starting_byte=self.Missing_Invalid_Data(Starting_byte,TestNumber,self.FTR_Rec_Summary,'Test_Txt')#;print('Des Text or lable:',Test_Txt)
            AlrmId,Starting_byte=self.Missing_Invalid_Data(Starting_byte,TestNumber,self.FTR_Rec_Summary,'AlrmId')#;print('Nmae of alaram :',AlrmId)
            ProgmTxt,Starting_byte=self.Missing_Invalid_Data(Starting_byte,TestNumber,self.FTR_Rec_Summary,'ProgmTxt')#;print('Addtional program info :',ProgmTxt)        
            RsltTxt,Starting_byte=self.Missing_Invalid_Data(Starting_byte,TestNumber,self.FTR_Rec_Summary,'RsltTxt')#;print('Addtional result info :',RsltTxt)
            Patrn_num,Starting_byte=self.U1(Starting_byte,1)#;print('Pattern generator number :',Patrn_num[0])
            #SpinMap,Starting_byte=self.DN(Starting_byte,1) if Starting_byte < self.End_Record_Byte else '', Starting_byte#;print('Bit map of enableed comprators :',SpinMap)
            if Starting_byte < self.End_Record_Byte: SpinMap,Starting_byte= self.DN(Starting_byte,1)
            else: SpinMap,Starting_byte= '', Starting_byte
        else:
            OptFlag=''#;print('Optional Flag :',OptFlag[0])
            Cycl_Cnt=''#;print('Vector Cycle count :',Cycl_Cnt[0])
            Rel_V_Addr=''#;print('Relative vector address :',Rel_V_Addr[0])
            Rept_C_Vctr=''#;print('Vector Repeat count :',Rept_C_Vctr[0])
            Num_P_Fail=''#;print('Pin count with 1 or more Failures',Num_P_Fail[0])
            X_Fail_Adrs=''#;print('X Logical dev Fail address :',X_Fail_Adrs[0])
            Y_Fail_Adrs=''#;print('Y Logical dev Fail address :',Y_Fail_Adrs[0])
            Vect_offset=''#;print('Offset from vector of intrest :',Vect_offset[0])
            Rtn_PmrIndex_cnt=''#;print('PMR indexes return data count :',Rtn_PmrIndex_cnt[0])
            Pgm_StateIndex=''#;print('Programed state index count :',Pgm_StateIndex[0])
            if (Rtn_PmrIndex_cnt==1 and Rtn_PmrIndex_cnt!=0): RTN_Index_ary,Starting_byte=self.U2(Starting_byte,1);RTN_State_ary,Starting_byte=self.U2(Starting_byte,1)
            elif Rtn_PmrIndex_cnt!="" and Rtn_PmrIndex_cnt>1:
                RTN_Index_ary=[]
                RTN_State_ary=[]
                for i in range(0,Rtn_PmrIndex_cnt): Array_val,Starting_byte=self.U2(Starting_byte,1);RTN_Index_ary.append(Array_val)
                for i in range(0,Rtn_PmrIndex_cnt): Array_val,Starting_byte=self.U2(Starting_byte,1);RTN_State_ary.append(Array_val)
            elif Rtn_PmrIndex_cnt==0 or  Rtn_PmrIndex_cnt=="":
                RTN_Index_ary=[]
                RTN_State_ary=[]
            RTN_Index_ary_str=','.join(str(e) for e in RTN_Index_ary)
            RTN_State_ary_str=','.join(str(e) for e in RTN_State_ary)
            if (Pgm_StateIndex==1 and Pgm_StateIndex!=0): Pgm_State_indx_ary,Starting_byte=self.U2(Starting_byte,1);Pgm_State_indx_ary_str=Pgm_State_indx_ary;Pgm_State_ary,Starting_byte=self.U2(Starting_byte,1);Pgm_State_ary_str=Pgm_State_ary
            elif Pgm_StateIndex!='' and Pgm_StateIndex>1:
                Pgm_State_indx_ary=[]
                Pgm_State_ary=[]
                for i in range(0,Pgm_StateIndex): Array_val,Starting_byte=self.U2(Starting_byte,1);Pgm_State_indx_ary.append(Array_val)
                for i in range(0,Pgm_StateIndex): Array_val,Starting_byte=self.U2(Starting_byte,1);Pgm_State_ary.append(Array_val)
            elif Pgm_StateIndex==0 or  Pgm_StateIndex=="":
                Pgm_State_indx_ary=[]
                Pgm_State_ary=[]
            Pgm_State_indx_ary_str=','.join(str(e) for e in Pgm_State_indx_ary)
            Pgm_State_ary_str=','.join(str(e) for e in Pgm_State_ary)
            Failpin=''#;print('Fail pin bit field :',Failpin,Starting_byte)
            VectNum=''#;print('Vect Module pattern name :',VectNum)
            Timesetname=''#;print('Time set name :',Timesetname)#[0].decode('utf-8'))
            opcode=''#;print('Vector Op code :',opcode)
            Test_Txt=''#;print('Des Text or lable:',Test_Txt)
            AlrmId=''#;print('Nmae of alaram :',AlrmId)
            ProgmTxt=''#;print('Addtional program info :',ProgmTxt)        
            RsltTxt=''#;print('Addtional result info :',RsltTxt)
            Patrn_num=''#;print('Pattern generator number :',Patrn_num[0])
            SpinMap=''#;print('Bit map of enableed comprators :',SpinMap)
        TestName=Test_Txt
        ## TestFlag_Info
        Alarm_Detected_during_testing= True if TestFlag[7:8]=='1' else False# Bit0
        Test_result_is_reliable= True if TestFlag[5:6]=='0' else False#Bit2
        Time_out_occured= True if TestFlag[4:5]=='1' else False#Bit3
        Test_exicuted= True if TestFlag[3:4]=='0' else False#Bit4
        Test_aborted= True if TestFlag[2:3]=='1' else False#Bit5
        Test_passed = (True if TestFlag[0:1]=='0' else False) if TestFlag[1:2]=='0' else 'Invalid'#Bit6,7

        if str(TestNumber)+";"+TestName not in self.TestNumbers:
            self.TestNumbers[str(TestNumber)+";"+TestName]= self.Record_Number
            self.Full_Rec_Summary[str(TestNumber)+";"+TestName]=[]
            self.Full_FIELD_LIST.append(str(TestNumber)+";"+TestName)
            self.Temp_Rec_Summary[str(TestNumber)+";"+TestName]=[]
            Dummy_list=[]
            if len(self.Full_Rec_Summary['File_Name'])>=1:
                for i in range(len(self.Full_Rec_Summary['File_Name'])) : Dummy_list.append(nan)
                self.Full_Rec_Summary[str(TestNumber)+";"+TestName].extend(Dummy_list)
                Dummy_list=[]
            for i in range(Number_of_Tested_devices_per_instant_count) : Dummy_list.append(nan)
            self.Temp_Rec_Summary[str(TestNumber)+";"+TestName].extend(Dummy_list)            
        elif self.Lists_in_Temp_Rec_Summary_are_empty==True and str(TestNumber)+";"+TestName in self.TestNumbers:
            Dummy_list=[]
            for i in range(Number_of_Tested_devices_per_instant_count) : Dummy_list.append(nan)
            for j in range(self.Full_FIELD_LIST.index('PartFix')+1,len(self.Full_FIELD_LIST)): self.Temp_Rec_Summary[self.Full_FIELD_LIST[j]].extend(Dummy_list)
            self.Lists_in_Temp_Rec_Summary_are_empty=False
        self.FTR_Field_List=[['File_Name',self.STDF_File.name],['Record_number',self.Record_Number],['TestNumber',TestNumber],['TestHeadNumber',TestHeadNumber],['SiteNumber',SiteNumber],['TestFlag',TestFlag],['OptFlag',OptFlag],['Cycl_Cnt',Cycl_Cnt],['Rel_V_Addr',Rel_V_Addr],['Rept_C_Vctr',Rept_C_Vctr],
        ['Num_P_Fail', Num_P_Fail],['X_Fail_Adrs',X_Fail_Adrs],['Y_Fail_Adrs',Y_Fail_Adrs],['Vect_offset',Vect_offset],['Rtn_PmrIndex_cnt',Rtn_PmrIndex_cnt],['Pgm_StateIndex',Pgm_StateIndex],['RTN_Index_ary_str',RTN_Index_ary_str],['RTN_State_ary_str',RTN_State_ary_str],['Pgm_State_indx_ary_str',Pgm_State_indx_ary_str],['Pgm_State_ary_str',Pgm_State_ary_str],['Failpin',Failpin],['VectNum',VectNum],['Timesetname',Timesetname],['opcode',opcode],['Test_Txt',Test_Txt],
        ['AlrmId',AlrmId],['ProgmTxt',ProgmTxt],['RsltTxt',RsltTxt],['Patrn_num',Patrn_num],['SpinMap',SpinMap],['Alarm_Detected_during_testing',Alarm_Detected_during_testing],
        ['Test_result_is_reliable',Test_result_is_reliable],['Time_out_occured',Time_out_occured],['Test_exicuted',Test_exicuted],['Test_aborted',Test_aborted],['Test_passed',Test_passed]]		
        for i in range(len(self.FTR_Field_List)): self.FTR_Rec_Summary[self.FTR_Field_List[i][0]].append(self.FTR_Field_List[i][1])
        for i in range(Number_of_Tested_devices_per_instant_count):
            if len(self.Temp_Rec_Summary[str(TestNumber)+";"+TestName])<=len(self.Temp_Rec_Summary['File_Name']) and self.Temp_Rec_Summary['TestHeadnumber'][i]==TestHeadNumber and self.Temp_Rec_Summary['TestSiteNumber'][i]==SiteNumber and self.Temp_Rec_Summary[str(TestNumber)+";"+TestName][i] is nan: self.Temp_Rec_Summary[str(TestNumber)+";"+TestName][i]=TestResult; break        
        return Starting_byte
    def PRR(self,Starting_byte):
        '''Function: Contains the result information relating to each part tested by the test program. The PRR and the Part Information Record (PIR) bracket all the stored information
            pertaining to one tested part.'''  
        global Number_of_resulted_dev_count
        HeadNum,Starting_byte=self.U1(Starting_byte,1)#;print('Test Head Number :',HeadNum[0])
        SiteNum,Starting_byte=self.U1(Starting_byte,1)#;print('Test Site Number :',SiteNum[0])
        Part_Flag,Starting_byte=self.B1(Starting_byte,1)#;print('Part info Flag :',bin(int.from_bytes(Part_Flag[0], byteorder=sys.byteorder)))
        Num_Test,Starting_byte=self.U2(Starting_byte,1)#;print('Number of tests executed :',Num_Test[0])
        HardBin,Starting_byte=self.U2(Starting_byte,1)#;print('Hardware Bin Number :',HardBin[0])
        SoftBin,Starting_byte=self.U2(Starting_byte,1)#;print('Software Bin Number :',SoftBin[0])
        XCo_ord,Starting_byte=self.I2(Starting_byte,1)#;print('X co-ordinate :',XCo_ord[0])
        YCo_ord,Starting_byte=self.I2(Starting_byte,1)#;print("Y Co-Oridinate :",YCo_ord[0])
        if XCo_ord==-32768: XCo_ord="N/A"
        if YCo_ord==-32768: YCo_ord="N/A"
        Testtime,Starting_byte=self.U4(Starting_byte,1)#;print('Test time in mil sec :',Testtime[0])
        PartId,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print('Part identification :',PartId[0].decode('utf-8'))        
        Part_Dis_Txt,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print('Part Description :',Part_Dis_Txt)
        if Starting_byte >= self.End_Record_Byte: PartFix,Starting_byte='',Starting_byte  
        elif Starting_byte < self.End_Record_Byte: PartFix,Starting_byte=self.BN(Starting_byte,1)#;print('Part repair Info :',PartFix)
        IsNewPart= True if (Part_Flag[7:8]=='0' and Part_Flag[6:7]=='0') else False
        Abnormal_end_of_testing= True if Part_Flag[5:6]=='1' else False
        Device_info=('Pass' if Part_Flag[4:5]=='0' else 'Fail') if Part_Flag[3:4]=='0' else 'Invalid'

        if Starting_byte > self.End_Record_Byte:  PartFix,Starting_byte='',Starting_byte
        else: PartFix,Starting_byte=self.BN(Starting_byte,1)
        self.PRR_Field_List=[['Part_Flag',Part_Flag],['Num_Test',Num_Test],['HardBin',str(HardBin)],['SiteNum',SiteNum],['SoftBin',str(SoftBin)],['Abnormal_end_of_testing',Abnormal_end_of_testing],['IsNewPart',IsNewPart],['Hbin_Num:Name',None],['Sbin_Num:Name',None],['XCo_ord',XCo_ord],['YCo_ord',YCo_ord],['Testtime',Testtime],['PartId',PartId],['Part_Dis_Txt',Part_Dis_Txt],['PartFix',PartFix],['File_Name',self.STDF_File.name]
        ,['Device_info',Device_info],['HeadNum',HeadNum]]
        if PartId not in self.Part_id_Index: self.Part_id_Index[PartId]=[len(self.Full_Rec_Summary['IsNewPart'])]
        elif PartId in self.Part_id_Index: self.Part_id_Index[PartId].append(len(self.Full_Rec_Summary['IsNewPart']))
        for i in range(len(self.PRR_Field_List)): self.PRR_Rec_Summary[self.PRR_Field_List[i][0]].append(self.PRR_Field_List[i][1])
        for i in range(23,38):
            if i!=26 and i!= 28: self.Temp_Rec_Summary[self.Full_FIELD_LIST[i]].append(self.PRR_Field_List[i-23][1])
        
        if self.Record_Details_list[1][self.Record_Number-1]!='PRR': Number_of_resulted_dev_count=1
        elif self.Record_Details_list[1][self.Record_Number-1]=='PRR': Number_of_resulted_dev_count+=1  
        if Number_of_resulted_dev_count==Number_of_Tested_devices_per_instant_count:
            for key in self.Full_Rec_Summary.keys():
                self.Full_Rec_Summary[key].extend(self.Temp_Rec_Summary[key])
                self.Temp_Rec_Summary[key].clear()
            self.Lists_in_Temp_Rec_Summary_are_empty=True
        return Starting_byte
    def WRR(self,Starting_byte):
        '''Reads the Wafer Result Record (WRR) from the STDF.  Contains the result information relating to each wafer tested by the job plan. The WRR
            and the Wafer Information Record (WIR) bracket all the stored information pertaining to one tested wafer. This record is used only when testing at wafer probe time. A
            WIR/WRR pair will have the same HEAD_NUM and SITE_GRP values.'''
        HeadNum,Starting_byte=self.U1(Starting_byte,1)#;print('Test Head Number:',HeadNum[0])
        Site_Grp,Starting_byte=self.U1(Starting_byte,1)#;print('Site Group Number:',Site_Grp[0])
        Finish_t,Starting_byte=self.U4(Starting_byte,1)#;print('Date and Time last part tested:',Finish_t[0])
        Part_Cnt,Starting_byte=self.U4(Starting_byte,1)#;print('Number of parts tested:',Part_Cnt[0])
        Rtst_Cnt,Starting_byte=self.U4(Starting_byte,1)#;print('Number of retested Parts :',Rtst_Cnt[0])
        Abrt_cnt,Starting_byte=self.U4(Starting_byte,1)#;print('Number of aborts during testing:',Abrt_cnt[0])
        Good_cnt,Starting_byte=self.U4(Starting_byte,1)#;print('Number of good parts:',Good_cnt[0])
        Func_Cnt,Starting_byte=self.U4(Starting_byte,1)#;print('Number of Functional tests:',Func_Cnt[0])
        Wafer_id,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print('Wafer id:',Wafer_id[0])
        Fabwf_id,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print('Fab WaferId:',Fabwf_id)
        Frame_id,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print('Wafer Frame Id:',Frame_id)
        Mask_id,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print('Wafer Mask id:',Mask_id)
        Usr_desc,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print('wafer description suplied by user:',Usr_desc)
        Exc_Desc,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print('Wafer description suplied by exec:',Exc_Desc)
        self.WRR_FIELD_LIST=[['File_Name',self.STDF_File.name],['HeadNum',HeadNum],['Site_Grp',Site_Grp],['Finish_t',Finish_t],['Part_Cnt',Part_Cnt],['Rtst_Cnt',Rtst_Cnt],['Abrt_cnt',Abrt_cnt],['Good_cnt',Good_cnt],
        ['Func_Cnt',Func_Cnt],['Wafer_id',Wafer_id],['Fabwf_id',Fabwf_id],['Frame_id',Frame_id],['Mask_id',Mask_id],['Usr_desc',Usr_desc],['Exc_Desc',Exc_Desc]]        
        for i in range(len(self.WRR_FIELD_LIST)): self.WRR_Rec_Summary[self.WRR_FIELD_LIST[i][0]].append(self.WRR_FIELD_LIST[i][1])
        return Starting_byte
    def TSR(self,Starting_byte):
        '''Reads the Test Summary Record from the STDF.
            Contains the test execution and failure counts for one parametric or functional test in
            the test program. Also contains static information, such as test name. The TSR is
            related to the Functional Test Record (FTR), the Parametric Test Record (PTR), and the
            Multiple Parametric Test Record (MPR) by test number, head number, and site
            number.'''
        HeadNum,Starting_byte=self.U1(Starting_byte,1)#;print('Test Head Num:',HeadNum[0])
        SiteNum,Starting_byte=self.U1(Starting_byte,1)#;print('Test Site Numebr:',SiteNum[0])
        Test_type,Starting_byte=self.C1(Starting_byte,1)#;print('Test type:',Test_type)
        Test_Num,Starting_byte=self.U4(Starting_byte,1)#;print('Test Number:',Test_Num)
        Exec_Cnt,Starting_byte=self.U4(Starting_byte,1)#;print('Nunber of test Executions:',Exec_Cnt)
        Fail_Cnt,Starting_byte=self.U4(Starting_byte,1)#;print('Number of test failures:',Fail_Cnt)
        Alarm_Cnt,Starting_byte=self.U4(Starting_byte,1)#;print('Number of alarmed tests:',Alarm_Cnt)
        Test_nam,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.TSR_Rec_Summary,'Test_nam')#;print('Test Name:',Test_nam[0])
        Seq_nam,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.TSR_Rec_Summary,'Seq_nam')#;print('Frogram flow name:',Seq_nam)
        Test_lbl,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.TSR_Rec_Summary,'Test_lbl')#;print('Test lable:',Test_lbl)
        if Starting_byte<self.End_Record_Byte:
            Opt_Flag,Starting_byte=self.B1(Starting_byte,1)#;print('Optional data flag:',Opt_Flag)
            Test_tim,Starting_byte=self.R4(Starting_byte,1)#;print('avg test execu time:',Test_tim)
            Test_min,Starting_byte=self.R4(Starting_byte,1)#;print('Lowest test result value:',Test_min)
            Test_max,Starting_byte=self.R4(Starting_byte,1)#;print('highst test result value:',Test_max)
            Test_sums,Starting_byte=self.R4(Starting_byte,1)#;print('Sum of test result values:',Test_sums)
            Test_sqrs,Starting_byte=self.R4(Starting_byte,1)#;print('Sum of squares of test result val:',Test_sqrs)
        elif Starting_byte>=self.End_Record_Byte:
            Opt_Flag=''#;print('Optional data flag:',Opt_Flag)
            Test_tim=''#;print('avg test execu time:',Test_tim)
            Test_min=''#;print('Lowest test result value:',Test_min)
            Test_max=''#;print('highst test result value:',Test_max)
            Test_sums=''#;print('Sum of test result values:',Test_sums)
            Test_sqrs=''
        self.TSR_FIELD_LIST=[['File_Name',self.STDF_File.name],['HeadNum',HeadNum],['SiteNum',SiteNum],['Test_type',Test_type],['TestNumber',Test_Num],['Exec_Cnt',Exec_Cnt],['Fail_Cnt',Fail_Cnt],['Alarm_Cnt',Alarm_Cnt],['Test_nam',Test_nam],
        ['Seq_nam',Seq_nam],['Test_lbl',Test_lbl],['Opt_Flag',Opt_Flag],['Test_tim',Test_tim],['Test_min',Test_min],['Test_max',Test_max],['Test_sums',Test_sums],['Test_sqrs',Test_sqrs],['Record_number',self.Record_Number]]
        for i in range(len(self.TSR_FIELD_LIST)): self.TSR_Rec_Summary[self.TSR_FIELD_LIST[i][0]].append(self.TSR_FIELD_LIST[i][1])
        
        return Starting_byte
    def HBR(self,Starting_byte):
        ''' Reads the Hardware Bin Record From the STDF.
            Stores a count of the parts “physically” placed in a particular bin after testing. (In wafer testing, “physical” binning is not an actual transfer of the chip, but rather is
            represented by a drop of ink or an entry in a wafer map file.) This bin count can be for  a single test site (when parallel testing) or a total for all test sites. The STDF
            specification also supports a Software Bin Record (SBR) for logical binning categories. A part is “physically” placed in a hardware bin after testing. A part can be “logically”
            associated with a software bin during or after testing.'''
        HeadNum,Starting_byte=self.U1(Starting_byte,1)#;print('Test Head Num:',HeadNum[0])
        SiteNum,Starting_byte=self.U1(Starting_byte,1)#;print('Test Site Numebr:',SiteNum[0])
        HbinNum,Starting_byte=self.U2(Starting_byte,1)#;print('Hardware bin:',HbinNum)
        if HbinNum==65535:
            HbinNum=65535
        Hbin_Cnt,Starting_byte=self.U4(Starting_byte,1)#;print('Number of parts in bin:',Hbin_Cnt)
        Hbin_Pf,Starting_byte=self.C1(Starting_byte,1)#;print('Pass/Fail Indication:',Hbin_Pf)
        Hbin_nam,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print('Name of hardware bin:',Hbin_nam)
        self.HBR_FIELD_LIST=[['File_Name',self.STDF_File.name],['HeadNum',HeadNum],['SiteNum',SiteNum],['HbinNum',str(HbinNum)],['Hbin_Cnt',Hbin_Cnt],['Hbin_Pf',Hbin_Pf],['Hbin_nam',Hbin_nam]]
        self.HBR_FIELD_LIST1=[['File_Name',self.STDF_File.name],['HeadNum',''],['SiteNum',''],['HbinNum','65535'],['Hbin_Cnt',''],['Hbin_Pf','F'],['Hbin_nam','']]
        if len(self.HBR_Rec_Summary['File_Name'])==0: 
            for i in range(len(self.HBR_FIELD_LIST)): self.HBR_Rec_Summary[self.HBR_FIELD_LIST[i][0]].append(self.HBR_FIELD_LIST1[i][1])
        for i in range(len(self.HBR_FIELD_LIST)): self.HBR_Rec_Summary[self.HBR_FIELD_LIST[i][0]].append(self.HBR_FIELD_LIST[i][1])        
        #self.HBR_FIELD_LIST=[self.STDF_File.name,'','',HbinNum,Hbin_Cnt,Hbin_Pf,Hbin_nam]
        return Starting_byte
    def SBR(self,Starting_byte):
        ''' Reads the Software Bin Record From the STDF.
            Stores a count of the parts associated with a particular logical bin after testing. This
            bin count can be for a single test site (when parallel testing) or a total for all test sites.
            The STDF specification also supports a Hardware Bin Record (HBR) for actual physical
            binning. A part is “physically” placed in a hardware bin after testing. A part can be
            “logically” associated with a software bin during or after testing.'''
        HeadNum,Starting_byte=self.U1(Starting_byte,1)#;print('Test Head Num:',HeadNum[0])
        SiteNum,Starting_byte=self.U1(Starting_byte,1)#;print('Test Site Numebr:',SiteNum[0])
        SbinNum,Starting_byte=self.U2(Starting_byte,1)#;print('Hardware bin:',SbinNum)
        Sbin_Cnt,Starting_byte=self.U4(Starting_byte,1)#;print('Number of parts in bin:',Sbin_Cnt)
        Sbin_Pf,Starting_byte=self.C1(Starting_byte,1)##;print('Pass/Fail Indication:',Sbin_Pf)
        Sbin_nam,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print('Name of hardware bin:',Sbin_nam)
        self.SBR_FIELD_LIST=[['File_Name',self.STDF_File.name],['HeadNum',HeadNum],['SiteNum',SiteNum],['SbinNum',str(SbinNum)],['Sbin_Cnt',Sbin_Cnt],['Sbin_Pf',Sbin_Pf],['Sbin_nam',Sbin_nam]]
        self.SBR_FIELD_LIST1=[['File_Name',self.STDF_File.name],['HeadNum',''],['SiteNum',''],['SbinNum','65535'],['Sbin_Cnt',''],['Sbin_Pf','F'],['Sbin_nam','']]
        if len(self.SBR_Rec_Summary['File_Name'])==0: 
            for i in range(len(self.SBR_FIELD_LIST)): self.SBR_Rec_Summary[self.SBR_FIELD_LIST[i][0]].append(self.SBR_FIELD_LIST1[i][1])
        for i in range(len(self.SBR_FIELD_LIST)): self.SBR_Rec_Summary[self.SBR_FIELD_LIST[i][0]].append(self.SBR_FIELD_LIST[i][1])
        return Starting_byte
    def PCR(self,Starting_byte):
        HeadNum,Starting_byte=self.U1(Starting_byte,1)#;print('Test Head Num:',HeadNum[0])
        SiteNum,Starting_byte=self.U1(Starting_byte,1)#;print('Test Site Numebr:',SiteNum[0])
        Part_cnt,Starting_byte=self.U4(Starting_byte,1)#;print('Num of parts:',Part_cnt[0])
        Rtst_Cnt,Starting_byte=self.U4(Starting_byte,1)#;print('Num of restested parts:',Rtst_Cnt)
        Abrt_Cnt,Starting_byte=self.U4(Starting_byte,1)#;print('Number of aborts during testing:',Abrt_Cnt)
        Good_Cnt,Starting_byte=self.U4(Starting_byte,1)#;print('Number of good parts:',Good_Cnt)
        Func_Cnt,Starting_byte=self.U4(Starting_byte,1)#;print('Number of Func parts tested',Func_Cnt)
        self.PCR_FIELD_LIST=[['File_Name',self.STDF_File.name],['HeadNum',HeadNum],['SiteNum',SiteNum],['Part_cnt',Part_cnt],['Rtst_Cnt',Rtst_Cnt],['Abrt_Cnt',Abrt_Cnt],['Good_Cnt',Good_Cnt],['Func_Cnt',Func_Cnt]]
        for i in range(len(self.PCR_FIELD_LIST)): self.PCR_Rec_Summary[self.PCR_FIELD_LIST[i][0]].append(self.PCR_FIELD_LIST[i][1])
        return Starting_byte
    def MRR(self,Starting_byte):

        Finist_Time,Starting_byte=self.U4(Starting_byte,1)#;print('finsish time:',Finist_Time[0])
        Disp_Cod,Starting_byte=self.Zero_len_byte(Starting_byte,self.C1)#;print('Lot Disposition code:',Disp_Cod)
        USr_Desc,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'USr_Desc')#;print('Lot dscription suplied by user:',USr_Desc)
        Exc_Desc,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'',self.MRR_Rec_Summary,'Exc_Desc')#;print('Lot description suplied by sys',Exc_Desc)
        self.MRR_FIELD_LIST=[['File_Name',self.STDF_File.name],['Finist_Time',Finist_Time],['Disp_Cod',Disp_Cod],['USr_Desc',USr_Desc],['Exc_Desc',Exc_Desc]]
        for i in range(len(self.MRR_FIELD_LIST)): self.MRR_Rec_Summary[self.MRR_FIELD_LIST[i][0]].append(self.MRR_FIELD_LIST[i][1])        
        self.Final_call_after_finishing_all_records()
        return Starting_byte
    def Final_call_after_finishing_all_records(self):
        ''' This function inserted to perform any modifications before closing the stdf file and going to csv'''
        for i in range(len(self.Full_Rec_Summary['HardBin'])):            
            if len(self.HBR_Rec_Summary['HbinNum'])!=0 :self.Full_Rec_Summary['Hbin_nam'].append(self.HBR_Rec_Summary['Hbin_nam'][self.HBR_Rec_Summary['HbinNum'].index(self.Full_Rec_Summary['HardBin'][i])])
            else:self.Full_Rec_Summary['Hbin_nam'].append(nan)            
            if len(self.HBR_Rec_Summary['HbinNum']) !=0 :self.Full_Rec_Summary['Hbin_Num:Name'][i]=(self.Full_Rec_Summary['HardBin'][i]+":"+self.HBR_Rec_Summary['Hbin_nam'][self.HBR_Rec_Summary['HbinNum'].index(self.Full_Rec_Summary['HardBin'][i])])
            else:self.Full_Rec_Summary['Hbin_Num:Name'][i]=(nan)
            if len(self.SBR_Rec_Summary['SbinNum'])!=0 :self.Full_Rec_Summary['Sbin_nam'].append(self.SBR_Rec_Summary['Sbin_nam'][self.SBR_Rec_Summary['SbinNum'].index(self.Full_Rec_Summary['SoftBin'][i])])
            else:self.Full_Rec_Summary['Sbin_nam'].append(nan)
            if len(self.SBR_Rec_Summary['SbinNum'])!=0 :self.Full_Rec_Summary['Sbin_Num:Name'][i]=(self.Full_Rec_Summary['SoftBin'][i]+":"+self.SBR_Rec_Summary['Sbin_nam'][self.SBR_Rec_Summary['SbinNum'].index(self.Full_Rec_Summary['SoftBin'][i])])
            else:self.Full_Rec_Summary['Sbin_Num:Name'][i]=(nan)
        #if self.Full_Rec_Summary['IsNewPart'][i]==True: self.Full_Rec_Summary['Re-test'][i]=0        
        for i in self.Full_Rec_Summary['File_Name']: self.Full_Rec_Summary['Re-test'].append('')
        for i in self.Part_id_Index.keys():
            if len(self.Part_id_Index[i])>1:
                for j in self.Part_id_Index[i]:
                    self.Full_Rec_Summary['Re-test'][j]= 0 if j==self.Part_id_Index[i][-1] else 1
            elif len(self.Part_id_Index[i])==1:
                self.Full_Rec_Summary['Re-test'][self.Full_Rec_Summary['PartId'].index(i)]= 0 #if j==self.Part_id_Index[len(self.Part_id_Index)-1] else 1
        for i in range(len(self.TSR_Rec_Summary['File_Name'])):
            if self.TSR_Rec_Summary['TestNumber'][i] not in self.TSR_Final_Test_details[0]:
                self.TSR_Final_Test_details[0].append(self.TSR_Rec_Summary['TestNumber'][i])
                self.TSR_Final_Test_details[1].append(self.TSR_Rec_Summary['HeadNum'][i])
                self.TSR_Final_Test_details[2].append(i)
            elif self.TSR_Rec_Summary['TestNumber'][i] in self.TSR_Final_Test_details[0] and self.TSR_Rec_Summary['HeadNum'][i]==255:
                self.TSR_Final_Test_details[1][self.TSR_Final_Test_details[0].index(self.TSR_Rec_Summary['TestNumber'][i])]=self.TSR_Rec_Summary['HeadNum'][i]
                self.TSR_Final_Test_details[2][self.TSR_Final_Test_details[0].index(self.TSR_Rec_Summary['TestNumber'][i])]=i
            elif self.TSR_Rec_Summary['TestNumber'][i] in self.TSR_Final_Test_details[0] and self.TSR_Rec_Summary['HeadNum'][i]!=255:
                self.TSR_Rec_Summary['Fail_Cnt'][self.TSR_Final_Test_details[0].index(self.TSR_Rec_Summary['TestNumber'][i])]+=self.TSR_Rec_Summary['Fail_Cnt'][i]
                #self.TSR_Final_Test_details[1][self.TSR_Final_Test_details[0].index(self.TSR_Rec_Summary['TestNumber'][i])]=self.TSR_Rec_Summary['HeadNum'][i]
                #self.TSR_Final_Test_details[2][self.TSR_Final_Test_details[0].index(self.TSR_Rec_Summary['TestNumber'][i])]=i
        for key in self.TSR_Rec_Summary.keys():
            print(key, len(self.TSR_Rec_Summary[key]))
        for key in self.TSR_Rec_Summary.keys():
            j=0
            for i in range(len(self.TSR_Rec_Summary[key])):
                if i not in self.TSR_Final_Test_details[2]:
                    kk=self.TSR_Rec_Summary[key].pop(i-j)
                    j+=1
    def BPS(self,Starting_byte):
        Seq_name,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','') #print('Program sec rec',Seq_name)
        self.BPS_FIELD_LIST=[['Seq_name',Seq_name]]
        self.BPS_Rec_Summary['Seq_name'].append(Seq_name);self.BPS_Rec_Summary["File_Name"].append(self.STDF_File.name)
        return(Starting_byte)
    def DTR(self,Starting_byte):
        TEXT_DAT,Starting_byte=self.CN(Starting_byte,1)#;print('Ascii text sring',TEXT_DAT)
        self.DTR_FIELD_LIST=[['TEXT_DAT',TEXT_DAT]]
        self.DTR_Rec_Summary['TEXT_DAT'].append(TEXT_DAT);self.DTR_Rec_Summary["File_Name"].append(self.STDF_File.name)
        return(Starting_byte)
    def EPS(self,Starting_byte):
        print(Starting_byte+'this is EPS record check if you want')
        return(Starting_byte)
    def GDR(self,Starting_byte):
        Fld_Cnt,Starting_byte=self.U2(Starting_byte,1)#;print('countof data fileds in record',Fld_Cnt)
        GDR_Summary=[]
        for i in range(Fld_Cnt):
            Gen_Data,Starting_byte=self.I1(Starting_byte,1)#;print('Gen data %i'%i ,Gen_Data)
            Rc=self.VN_MAP[str(Gen_Data)]
            temp,Starting_byte=Rc(self,Starting_byte,1)#;print(temp) 
            final=('Gen data %i'%i ,temp)#;print(final)
            GDR_Summary.append(final)
        GDR_Summary_str=','.join(str(e) for e in GDR_Summary)
        self.GDR_FIELD_LIST=[['Fld_Cnt',Fld_Cnt],['GDR_Summary_str',GDR_Summary_str]]
        self.GDR_Rec_Summary["File_Name"].append(self.STDF_File.name);self.GDR_Rec_Summary["Fld_Cnt"].append(Fld_Cnt);self.GDR_Rec_Summary["GDR_Summary_str"].append(GDR_Summary_str)
        return(Starting_byte)
    def PGR(self,Starting_byte):
        Grp_index,Starting_byte=self.U2(Starting_byte,1)#;print('Uniq index associated with pin grp',Grp_index)
        GRP_NAM,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')#;print('name of pin grop',GRP_NAM)
        INDX_CNT,Starting_byte=self.U2(Starting_byte,1)#;print('cont of k ',INDX_CNT)
        if (INDX_CNT==1 and INDX_CNT!=0): PMR_INDX,Starting_byte=self.U2(Starting_byte,INDX_CNT)
        elif INDX_CNT>1:
            PMR_INDX=[]
            for i in range(0,INDX_CNT): Array_val,Starting_byte=self.U2(Starting_byte,1);PMR_INDX.append(Array_val)        
        elif INDX_CNT==0 or  INDX_CNT=="":
            PMR_INDX=[]
        PMR_INDX_str=','.join(str(e) for e in PMR_INDX)
        self.PGR_FIELD_LIST=[['File_Name',self.STDF_File.name],['Grp_index',Grp_index],['GRP_NAM',GRP_NAM],['INDX_CNT',INDX_CNT],['PMR_INDX_str',PMR_INDX_str]] 
        for i in range(len(self.PGR_FIELD_LIST)): self.PGR_Rec_Summary[self.PGR_FIELD_LIST[i][0]].append(self.PGR_FIELD_LIST[i][1])
        return Starting_byte
    def PLR(self,Starting_byte):
        self.Grp_Cnt,Starting_byte=self.U2(Starting_byte,1)#;print('count of k',Grp_Cnt)
        if (self.Grp_Cnt==1 and self.Grp_Cnt!=0): self.Grp_indx,Starting_byte=self.U2(Starting_byte,self.Grp_Cnt) 
        elif self.Grp_Cnt>1:
            self.Grp_indx=[]
            for i in range(0,self.Grp_Cnt): Array_val,Starting_byte=self.U2(Starting_byte,1);self.Grp_indx.append(Array_val)  
        if (self.Grp_Cnt==1 and self.Grp_Cnt!=0): self.GRP_MODE,Starting_byte=self.U2(Starting_byte,1) 
        elif self.Grp_Cnt>1:
            self.GRP_MODE=[]
            for i in range(0,self.Grp_Cnt): Array_val,Starting_byte=self.U2(Starting_byte,1);self.GRP_MODE.append(Array_val)
        if (self.Grp_Cnt==1 and self.Grp_Cnt!=0): self.GRP_RADX,Starting_byte=self.U1(Starting_byte,1) 
        elif self.Grp_Cnt>1:
            self.GRP_RADX=[]
            for i in range(0,self.Grp_Cnt): Array_val,Starting_byte=self.U1(Starting_byte,1);self.GRP_RADX.append(Array_val)
        if (self.Grp_Cnt==1 and self.Grp_Cnt!=0): self.PGM_CHAR,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','') 
        elif self.Grp_Cnt>1:
            self.PGM_CHAR=[]
            for i in range(0,self.Grp_Cnt): Array_val,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','');self.PGM_CHAR.append(Array_val)
        if (self.Grp_Cnt==1 and self.Grp_Cnt!=0): self.RTN_CHAR,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')
        elif self.Grp_Cnt>1:
            self.RTN_CHAR=[]
            for i in range(0,self.Grp_Cnt): Array_val,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','');self.RTN_CHAR.append(Array_val)
        if (self.Grp_Cnt==1 and self.Grp_Cnt!=0): self.PGM_CHAL,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','') 
        elif self.Grp_Cnt>1:
            self.PGM_CHAL=[]
            for i in range(0,self.Grp_Cnt): Array_val,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','');self.PGM_CHAL.append(Array_val)
        if (self.Grp_Cnt==1 and self.Grp_Cnt!=0): self.RTN_CHAL,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')
        elif self.Grp_Cnt>1:
            self.RTN_CHAL=[]
            for i in range(0,self.Grp_Cnt): Array_val,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','');self.RTN_CHAL.append(Array_val)
        return(Starting_byte)
    def RDR(self,Starting_byte):
        Num_bins,Starting_byte=self.U2(Starting_byte,1)#;print('nuber of bins k ',Num_bins)
        if (Num_bins==1 and Num_bins!=0): RTST_BIN,Starting_byte=self.U2(Starting_byte,Num_bins) 
        elif Num_bins>1:
            RTST_BIN=[]
            for i in range(0,Num_bins): Array_val,Starting_byte=self.U2(Starting_byte,1);RTST_BIN.append(Array_val)
        elif Num_bins==0 or  Num_bins=="":
            RTST_BIN=[]
        RTST_BIN_str=','.join(str(e) for e in RTST_BIN)
        self.RDR_FIELD_LIST=[['Num_bins',Num_bins],['RTST_BIN_str',RTST_BIN_str]]
        self.RDR_Rec_Summary["File_Name"].append(self.STDF_File.name);self.RDR_Rec_Summary["Num_bins"].append(Num_bins);self.RDR_Rec_Summary["RTST_BIN_str"].append(RTST_BIN_str)
        return Starting_byte
    def VUR(self,Starting_byte):
        '''Version update Record is used to identify the updates over version V4.
            Presence of this record indicates that the file may contain records defined by
            the new standard. This record is added to the major type 0 in the STDF V4.'''
        self.UPD_NAM,Starting_byte=self.CN(Starting_byte,1)
        self.VUR_FIELD_LIST=[["File_Name",self.STDF_File.name],['UPD_NAM',self.UPD_NAM]]
        
        return Starting_byte  
    def PSR(self,Starting_byte):
        #print(Starting_byte,self.Record_name,'refer to document on this')
        #Starting_byte=self.End_Record_Byte;return Starting_byte
        self.CONT_FLG,Starting_byte=self.B1(Starting_byte,1)
        self.PSR_INDX,Starting_byte=self.U2(Starting_byte,1)
        self.PSR_NAM,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','') 
        self.OPT_FLG,Starting_byte=self.B1(Starting_byte,1)
        self.TOTP_CNT,Starting_byte=self.U2(Starting_byte,1)
        self.LOCP_CNT,Starting_byte=self.U2(Starting_byte,1)
        #self.PAT_BGN,Starting_byte= 
        if (self.LOCP_CNT==1 and self.LOCP_CNT!=0): self.PAT_BGN,Starting_byte=self.U8(Starting_byte,self.LOCP_CNT) 
        elif self.LOCP_CNT>1:
            self.PAT_BGN=[]
            for i in range(0,self.LOCP_CNT): Array_val,Starting_byte=self.U8(Starting_byte,1);self.PAT_BGN.append(Array_val)
        #self.PAT_END,Starting_byte=
        if (self.LOCP_CNT==1 and self.LOCP_CNT!=0): self.PAT_END,Starting_byte=self.U8(Starting_byte,self.LOCP_CNT) 
        elif self.LOCP_CNT>1:
            self.PAT_END=[]
            for i in range(0,self.LOCP_CNT): Array_val,Starting_byte=self.U8(Starting_byte,1);self.PAT_END.append(Array_val)
        #self.PAT_FILE,Starting_byte=
        if (self.LOCP_CNT==1 and self.LOCP_CNT!=0): self.PAT_FILE,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')
        elif self.LOCP_CNT>1:
            self.PAT_FILE=[]
            for i in range(0,self.LOCP_CNT): Array_val,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','');self.PAT_FILE.append(Array_val)
        #self.PAT_LBL,Starting_byte=
        if (self.LOCP_CNT==1 and self.LOCP_CNT!=0): self.PAT_LBL,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')
        elif self.LOCP_CNT>1:
            self.PAT_LBL=[]
            for i in range(0,self.LOCP_CNT): Array_val,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','');self.PAT_LBL.append(Array_val) 
        #self.FILE_UID,Starting_byte=
        if (self.LOCP_CNT==1 and self.LOCP_CNT!=0): self.FILE_UID,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')
        elif self.LOCP_CNT>1:
            self.FILE_UID=[]
            for i in range(0,self.LOCP_CNT): Array_val,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','');self.FILE_UID.append(Array_val)
        #self.ATPG_DSC,Starting_byte=
        if (self.LOCP_CNT==1 and self.LOCP_CNT!=0): self.ATPG_DSC,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')
        elif self.LOCP_CNT>1:
            self.ATPG_DSC=[]
            for i in range(0,self.LOCP_CNT): Array_val,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','');self.ATPG_DSC.append(Array_val)
        #self.SRC_ID,Starting_byte=
        if (self.LOCP_CNT==1 and self.LOCP_CNT!=0): self.SRC_ID,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','')
        elif self.LOCP_CNT>1:
            self.SRC_ID=[]
            for i in range(0,self.LOCP_CNT): Array_val,Starting_byte=self.Missing_Invalid_Data(Starting_byte,'','','');self.SRC_ID.append(Array_val)
        self.PSR_FIELD_LIST=[["File_Name",self.STDF_File.name],['CONT_FLG',self.CONT_FLG],['PSR_INDX',self.PSR_INDX],['PSR_NAM',self.PSR_NAM],['OPT_FLG',self.OPT_FLG],['TOTP_CNT',self.TOTP_CNT],['LOCP_CNT',self.LOCP_CNT]]
        
        return Starting_byte
        #break
    def NMR(self,Starting_byte):
        self.CONT_FLG,Starting_byte=self.B1(Starting_byte,1)
        self.TOTM_CNT,Starting_byte=self.U2(Starting_byte,1)
        self.LOCM_CNT,Starting_byte=self.U2(Starting_byte,1)
        self.PMR_INDX,Starting_byte=self.KX_Looped_data(Starting_byte,self.U2,self.LOCM_CNT,'')
        self.ATPG_NAM,Starting_byte=self.KX_Looped_data(Starting_byte,self.CN,self.LOCM_CNT,'')    
        self.NMR_FIELD_LIST=[["File_Name",self.STDF_File.name],['CONT_FLG',self.CONT_FLG],['TOTM_CNT',self.TOTM_CNT],['LOCM_CNT',self.LOCM_CNT],['PMR_INDX',self.PMR_INDX],['ATPG_NAM',self.ATPG_NAM]]
    def CNR(self,Starting_byte):
        self.CHN_NUM,Starting_byte=self.U2(Starting_byte,1)
        self.BIT_POS,Starting_byte=self.U2(Starting_byte,1)
        self.CELL_NAM,Starting_byte=self.SN(Starting_byte,1)
        self.CNR_FIELD_LIST=[["File_Name",self.STDF_File.name],['CHN_NUM',self.CHN_NUM],['BIT_POS',self.BIT_POS],['CELL_NAM',self.CELL_NAM]]
    def SSR(self,Starting_byte):
        self.SSR_NAM,Starting_byte=self.CN(Starting_byte,1)
        self.CHN_CNT,Starting_byte=self.U2(Starting_byte,1)
        self.CHN_LIST,Starting_byte=self.KX_Looped_data(Starting_byte,self.U2,self.CHN_CNT,'')
        self.SSR_FIELD_LIST=[["File_Name",self.STDF_File.name],['SSR_NAM',self.SSR_NAM],['CHN_CNT',self.CHN_CNT],['CHN_LIST',self.CHN_LIST]]
    def SCR(self,Starting_byte):
        
        self.CONT_FLG,Starting_byte=self.B1(Starting_byte,1)
        self.CDR_INDX,Starting_byte=self.U2(Starting_byte,1)
        self.CHN_NAM,Starting_byte=self.CN(Starting_byte,1)
        self.CHN_LEN,Starting_byte=self.U4(Starting_byte,1)
        self.SIN_PIN,Starting_byte=self.U2(Starting_byte,1)
        self.SOUT_PIN,Starting_byte=self.U2(Starting_byte,1)
        self.MSTR_CNT,Starting_byte=self.U1(Starting_byte,1)
        self.M_CLKS,Starting_byte=self.KX_Looped_data(Starting_byte,self.U2,self.MSTR_CNT,'')
        self.SLAV_CNT,Starting_byte=self.B1(Starting_byte,1)
        self.S_CLKS,Starting_byte=self.KX_Looped_data(Starting_byte,self.U2,self.SLAV_CNT,'')
        self.INV_VAL,Starting_byte=self.B1(Starting_byte,1)
        self.LST_CNT,Starting_byte=self.B1(Starting_byte,1)
        self.CELL_LST,Starting_byte=self.KX_Looped_data(Starting_byte,self.SN,self.SLAV_CNT,'')
        self.SCR_FIELD_LIST=[["File_Name",self.STDF_File.name],['CONT_FLG',self.CONT_FLG],['CDR_INDX',self.CDR_INDX],['CHN_NAM',self.CHN_NAM],['CHN_LEN',self.CHN_LEN],['SIN_PIN',self.SIN_PIN],['SOUT_PIN',self.SOUT_PIN],['MSTR_CNT',self.MSTR_CNT],['M_CLKS',self.M_CLKS],['SLAV_CNT',self.SLAV_CNT],['S_CLKS',self.S_CLKS],['INV_VAL',self.INV_VAL],['LST_CNT',self.LST_CNT],['CELL_LST',self.CELL_LST]]    
    def STR(self,Starting_byte):
        '''Scan Test Record (STR) is a new record that is added to the major record type 15 category (Data Collected Per Test Execution).
            This is the same category where functional and parametric fail records exist. Thus the scan test record becomes another test record type in this category.
            It contains all or some of the results of the single execution of a scan test in  the test program. It is intended to contain all of the individual pin/cycle
            failures that are detected in a single test execution. If there are more failures than can be contained in a single record, then the record may be followed by
            additional continuation STR records. In this new record some fields have been brought over from the functional test
            record and some new fields have been added to handle the scan test data. Table 4 shows the structure of the STR at a conceptual level.'''
        self.CONT_FLG,Starting_byte=self.B1(Starting_byte,1)
        self.TEST_NUM,Starting_byte=self.U4(Starting_byte,1)
        self.HEAD_NUM,Starting_byte=self.U1(Starting_byte,1)        
        self.SITE_NUM,Starting_byte=self.U1(Starting_byte,1)
        self.PSR_REF,Starting_byte=self.U2(Starting_byte,1)
        self.TEST_FLG,Starting_byte=self.B1(Starting_byte,1)
        self.LOG_TYP,Starting_byte=self.CN(Starting_byte,1)
        self.TEST_TXT,Starting_byte=self.CN(Starting_byte,1)
        self.ALARM_ID,Starting_byte=self.CN(Starting_byte,1)
        self.PROG_TXT,Starting_byte=self.CN(Starting_byte,1)
        self.RSLT_TXT,Starting_byte=self.CN(Starting_byte,1)
        self.Z_VAL,Starting_byte=self.U1(Starting_byte,1)
        self.FMU_FLG,Starting_byte=self.B1(Starting_byte,1)
        self.MASK_MAP,Starting_byte=self.DN(Starting_byte,1) if int(self.FMU_FLG[7])==1 and int(self.FMU_FLG[6])==0  else '',Starting_byte # observed teh STDF spec sheet and update this else condition
        self.FAL_MAP,Starting_byte=self.DN(Starting_byte,1)  if int(self.FMU_FLG[5])==1 and int(self.FMU_FLG[4])==0  else '',Starting_byte # observed teh STDF spec sheet and update this else condition
        self.CYC_CNT,Starting_byte=self.U8(Starting_byte,1)
        self.TOTF_CNT,Starting_byte=self.U4(Starting_byte,1)
        self.TOTL_CNT,Starting_byte=self.U4(Starting_byte,1)
        self.CYC_BASE,Starting_byte=self.U8(Starting_byte,1)
        self.BIT_BASE,Starting_byte=self.U4(Starting_byte,1)
        self.COND_CNT,Starting_byte=self.U2(Starting_byte,1)
        self.LIM_CNT,Starting_byte=self.U2(Starting_byte,1)
        self.CYC_SIZE,Starting_byte=self.U1(Starting_byte,1)
        self.PMR_SIZE,Starting_byte=self.U1(Starting_byte,1)
        self.CHN_SIZE,Starting_byte=self.U1(Starting_byte,1)
        self.PAT_SIZE,Starting_byte=self.U1(Starting_byte,1)
        self.BIT_SIZE,Starting_byte=self.U1(Starting_byte,1)
        self.U1_SIZE,Starting_byte=self.U1(Starting_byte,1)
        self.U2_SIZE,Starting_byte=self.U1(Starting_byte,1)
        self.U3_SIZE,Starting_byte=self.U1(Starting_byte,1)
        self.UTX_SIZE,Starting_byte=self.U1(Starting_byte,1)
        if self.UTX_SIZE>0:
            self.UTX_SIZE=self.UTX_SIZE
        self.CAP_BGN,Starting_byte=self.U2(Starting_byte,1)
        self.LIM_INDX,Starting_byte=self.KX_Looped_data(Starting_byte,self.U2,self.LIM_CNT,'')
        self.LIM_SPEC,Starting_byte=self.KX_Looped_data(Starting_byte,self.U4,self.LIM_CNT,'')
        self.COND_LST,Starting_byte=self.KX_Looped_data(Starting_byte,self.CN,self.COND_CNT,'')
        self.CYC_CNT2,Starting_byte=self.U2(Starting_byte,1)
        self.CYC_OFST,Starting_byte=self.KX_Looped_data(Starting_byte,self.UF,int(self.CYC_CNT2)+int(self.CYC_BASE),int(self.CYC_SIZE))
        self.PMR_CNT,Starting_byte=self.U2(Starting_byte,1)
        self.PMR_INDX,Starting_byte=self.KX_Looped_data(Starting_byte,self.UF,int(self.PMR_CNT),int(self.PMR_SIZE))
        self.CHN_CNT,Starting_byte=self.U2(Starting_byte,1)
        self.CHN_NUM,Starting_byte=self.KX_Looped_data(Starting_byte,self.UF,int(self.CHN_CNT),int(self.CHN_SIZE))
        self.EXP_CNT,Starting_byte=self.U2(Starting_byte,1)
        self.EXP_DATA,Starting_byte=self.KX_Looped_data(Starting_byte,self.U1,int(self.EXP_CNT),'')
        self.CAP_CNT,Starting_byte=self.U2(Starting_byte,1)
        self.CAP_DATA,Starting_byte=self.KX_Looped_data(Starting_byte,self.U1,int(self.CAP_CNT),'')
        self.NEW_CNT,Starting_byte=self.U2(Starting_byte,1)
        self.NEW_DATA,Starting_byte=self.KX_Looped_data(Starting_byte,self.U1,self.NEW_CNT,'')
        self.PAT_CNT,Starting_byte=self.U2(Starting_byte,1)
        self.PAT_NUM,Starting_byte=self.KX_Looped_data(Starting_byte,self.UF,int(self.PAT_CNT),int(self.PAT_SIZE))
        self.BPOS_CNT,Starting_byte=self.U2(Starting_byte,1)
        self.BIT_POS,Starting_byte=self.KX_Looped_data(Starting_byte,self.UF,int(self.BPOS_CNT),int(self.BIT_SIZE))
        self.USR1_CNT,Starting_byte=self.U2(Starting_byte,1)       
        self.USR1,Starting_byte=self.KX_Looped_data(Starting_byte,self.UF,int(self.USR1_CNT),int(self.U1_SIZE))
        self.USR2_CNT,Starting_byte=self.U2(Starting_byte,1)
        self.USR2,Starting_byte=self.KX_Looped_data(Starting_byte,self.UF,int(self.USR2_CNT),int(self.U2_SIZE))
        self.USR3_CNT,Starting_byte=self.U2(Starting_byte,1)
        self.USR3,Starting_byte=self.KX_Looped_data(Starting_byte,self.UF,int(self.USR3_CNT),int(self.U3_SIZE))
        self.TXT_CNT,Starting_byte=self.U2(Starting_byte,1)        
        self.USER_TXT,Starting_byte=self.KX_Looped_data(Starting_byte,self.UF,int(self.TXT_CNT),int(self.UTX_SIZE))
        self.STR_FIELD_LIST=[["File_Name",self.STDF_File.name],['CONT_FLG',self.CONT_FLG],['TEST_NUM',self.TEST_NUM],['HEAD_NUM',self.HEAD_NUM],['SITE_NUM',self.SITE_NUM],['PSR_REF',self.PSR_REF],['TEST_FLG',self.TEST_FLG],['LOG_TYP',self.LOG_TYP],['TEST_TXT',self.TEST_TXT],['ALARM_ID',self.ALARM_ID],['PROG_TXT',self.PROG_TXT],['RSLT_TXT',self.RSLT_TXT],['Z_VAL',self.Z_VAL],['FMU_FLG',self.FMU_FLG],['MASK_MAP',self.MASK_MAP],['FAL_MAP',self.FAL_MAP],['CYC_CNT',self.CYC_CNT],['TOTF_CNT',self.TOTF_CNT],['TOTL_CNT',self.TOTL_CNT],['CYC_BASE',self.CYC_BASE],['BIT_BASE',self.BIT_BASE],['COND_CNT',self.COND_CNT],['LIM_CNT',self.LIM_CNT],['CYC_SIZE',self.CYC_SIZE],['PMR_SIZE',self.PMR_SIZE],['CHN_SIZE',self.CHN_SIZE],['PAT_SIZE',self.PAT_SIZE],['BIT_SIZE',self.BIT_SIZE],['U1_SIZE',self.U1_SIZE],['U2_SIZE',self.U2_SIZE],['U3_SIZE',self.U3_SIZE],['UTX_SIZE',self.UTX_SIZE],['CAP_BGN',self.CAP_BGN],['LIM_INDX',self.LIM_INDX],['LIM_SPEC',self.LIM_SPEC],['COND_LST',self.COND_LST],['CYC_CNT2',self.CYC_CNT2],['CYC_OFST',self.CYC_OFST],['PMR_CNT',self.PMR_CNT],['PMR_INDX',self.PMR_INDX],['CHN_CNT',self.CHN_CNT],['CHN_NUM',self.CHN_NUM],['EXP_CNT',self.EXP_CNT],['EXP_DATA',self.EXP_DATA],['CAP_CNT',self.CAP_CNT],['CAP_DATA',self.CAP_DATA],['NEW_CNT',self.NEW_CNT],['NEW_DATA',self.NEW_DATA],['PAT_CNT',self.PAT_CNT],['PAT_NUM',self.PAT_NUM],['BPOS_CNT',self.BPOS_CNT],['BIT_POS',self.BIT_POS],['USR1_CNT',self.USR1_CNT],['USR1',self.USR1],['USR2_CNT',self.USR2_CNT],['USR2',self.USR2],['USR3_CNT',self.USR3_CNT],['USR3',self.USR3],['TXT_CNT',self.TXT_CNT],['USER_TXT',self.USER_TXT]]
        #self.CYC_BASE,Starting_byte=
    #reading the data
    Record_Name_Functions={'FAR':FAR,'ATR':ATR,'MIR':MIR,'SDR':SDR,'PMR':PMR,'WCR':WCR,'WIR':WIR,'PIR':PIR,'PTR':PTR,'FTR':FTR,'PRR':PRR,'WRR':WRR,'TSR':TSR,
    'HBR':HBR,'SBR':SBR,'PCR':PCR,'MRR':MRR,'BPS':BPS,'DTR':DTR,'EPS':EPS,'GDR':GDR,'PGR':PGR,'PLR':PLR,'RDR':RDR,'MPR':MPR,'VUR':VUR,'NMR':NMR,'PSR':PSR,'CNR':CNR,'SSR':SSR,'SCR':SCR,'STR':STR}    
    
    @QtCore.pyqtSlot(int)
    def send_val(self):
        self.File_Load_Status.emit(5)
    def Encodethedata(self,Starting_byte):
        #from math import ceil
        Starting_byte=Starting_byte
        Size_of_Stdf_file=len(self.STDF_Data)
        while Starting_byte<Size_of_Stdf_file:
            try:
                Starting_byte=self.Record_header(Starting_byte)
                self.odd_nibble=True
                if  self.Record_Number==1029:
                    self.Record_Number=1029
                if self.Record_name[0] in self.Record_Name_Functions: 
                    Starting_byte=self.Record_Name_Functions[self.Record_name[0]](self,Starting_byte)
                    if Starting_byte!=self.End_Record_Byte: 
                        Starting_byte=self.End_Record_Byte
                        self.test=50
                else: print(self.Record_name,'Starting_byte:%s'%Starting_byte,'Record_number:%s'%self.Record_Number);break
            except:
                print('Oops!  I met with an error :() while decoding the current STDF please contact my Developer')#;STDF_Reading_completed=False
                print(self.Record_name,'Starting_byte:%s'%Starting_byte,'Record_number:%s'%self.Record_Number);quit()
        #Starting_byte>=len(self.STDF_Data)
        print('File reading completed')        
        '''for i in range(len(self.Record_summary_list)):
            g=self.Record_summary_list2[i]
            self.Record_summary_list[i]=self.pandas.DataFrame(self.Record_summary_list2[i])
            self.Record_summary_list[i].to_csv("%s.csv" %self.Record_summary_list[i])
        ptr=self.pandas.DataFrame(self.PTR_Rec_Summary)
        ftr=self.pandas.DataFrame(self.FTR_Rec_Summary)
        mpr=self.pandas.DataFrame(self.MPR_Rec_Summary)
        ptr.to_csv("ptr.csv")
        ftr.to_csv("ftr.csv")
        mpr.to_csv("mpr.csv")'''
        return
    def Convert_to_CSV(self,input):
        '''output=input
        output=output.split(".")[0]+".csv"
        with open(output,'w') as F:
            for i in range(0 , len(self.PartFullInfo)):
                print(self.PartFullInfo[i],file=F)
            for i in range(1 , len(self.FullTestDetails)):
                print(self.FullTestDetails[i],file=F)
        output=output.replace('.csv','_MIR.csv')
        with open(output,'w') as F:
            for i in range(0,len(self.MIR_Rec_Summary)):
                print(self.MIR_Rec_Summary[i],file=F)'''
        #import xlsxwriter
        extn=os.path.splitext(self.STDF_File.name)[-1].lower()
        '''workbook = self.xlsxwriter.Workbook(self.STDF_File.name.split(extn)[0]+'.csv')
        worksheet = workbook.add_worksheet()
        row = 0        
        for key in self.Full_Rec_Summary.keys():
            try:
                worksheet.write(0,row, key)
                worksheet.write_column(1,row, self.Full_Rec_Summary[key])
                row += 1
            except:
                print(key)
        workbook.close()'''
    def Start_process(self,Input_File,gui_name):
        Input_file=Input_File
        extn=os.path.splitext(Input_file)[-1].lower()
        
        if Input_file!="" and ( extn=='.std' or extn=='.stdf'):
            self.Load_the_file(Input_file)
            self.Encodethedata(0)
            #if STDF_Reading_completed==True: 
            self.Convert_to_CSV(Input_file)
            #return self.Clubbed_Record_Details
        else:
            print('There is some issue with the file selected please browse a proper file')
            #self.("Successful", "STDF to CSV Convertion is completed")
            #self.Stdf_Parser_Form.destroy()
        #else:
            #self.tkinter.messagebox.showinfo("Error", "Please Browse a File")
   # Start_process(self.Input_File)

    