from public import *
import qrcode


api=Blueprint('api',__name__)

@api.route('/ViewOut')
def ViewOut():
	data={}
	out=request.args['out']

	with open(compiled_contract_path) as file:
		contract_json = json.load(file)  # load contract info as JSON
		contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
	contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
	blocknumber = web3.eth.get_block_number()
	res = []
	# try:
	for i in range(blocknumber, 0, -1):
		a = web3.eth.get_transaction_by_block(i, 0)
		decoded_input = contract.decode_function_input(a['input'])
		print("add stock 11111111111111111")
		# print(decoded_input)
		if str(decoded_input[0]) == "<Function add_stock(uint256,uint256,uint256,uint256,uint256,uint256,string,string,string)>":
			
			print("oo0000",decoded_input[1]['stock_id'])
			if int(decoded_input[1]['stock_id']) == int(out):
				print("outssss",decoded_input[1])
				res.append(decoded_input[1])
		
	# except Exception as e:
	# 	print("", res)
	print("dfgdfgdfgdfgfgdfgfdgfdgfgdgdfgdggggggggggggggggggggg",res[0]['mid'])
	data['mfg']="MFG:"+res[0]['mfg']
	data['exp']="Exp:"+res[0]['date']	

	# print(res[0]['date'])

	q="select * from manufacture where login_id='%s'"%(res[0]['m_id'])
	# print("login:::::::::",q)
	res2=select(q)
	data['manu']="Name:"+res2[0]['name']
	data['manuplace']="place:"+res2[0]['place']

	q="select * from pharmacy where login_id='%s'"%(res[0]['pid'])
	res1=select(q)
	if res1:
		data['phar']="phar name:"+res1[0]['pharmacy_name']
		data['pharplace']="phar place:"+res1[0]['place']
	print("ddddddidssssssssssssss",res[0]['did'])
	q="select *,concat(fname,' ',lname) as dname from distributor where distributer_id='%s'"%(res[0]['did'])
	print(q)
	res1=select(q)
	if res1:
		data['dis']="dist name"+res1[0]['dname']
		data['displace']="dis place"+res1[0]['place']
		# print(res1[0][0])
	with open(compiled_contract_path) as file:
		contract_json = json.load(file)  # load contract info as JSON
		contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
	contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
	blocknumber = web3.eth.get_block_number()
	res2 = []
	try:
		for i in range(blocknumber, 0, -1):
			a = web3.eth.get_transaction_by_block(i, 0)
			decoded_input = contract.decode_function_input(a['input'])
			# print("dddddd",decoded_input)
			if str(decoded_input[0]) == "<Function add_medicine(uint256,uint256,uint256,string,string,string,string,string,string,string,string,string)>":
				# print("Geted",res[0]['mid'])
				# print("Decoded",decoded_input[0])
				if int(decoded_input[1]['medicine_id']) == int(res[0]['mid']):
					res2.append(decoded_input[1])

					# res.append(decoded_input['fn'])
				print(res2)
	except Exception as e:
		print("", e)
		pass
	print(res2)
	q="select * from medicine where medicine_id='%s' " %(res[0]['mid'])
	print(q)
	res3=select(q)
	

	data['medicine']="medicine name:"+res3[0]['name']
	data['description']="Description:"+res3[0]['description']


	


	data['status']="success"
	data['method']="ViewOut"
	
	return str(data)


@api.route('/Feedbacks',methods=['get','post'])
def Feedbacks():
	data={}
	feed=request.args['feed']
	users=request.args['users']
	

	q="INSERT INTO `feedback` VALUES(null,'%s','%s',curdate())"%(users,feed)
	id=insert(q)
	data['status']="success"
	data['method']="Feedbacks"
	return str(data)




@api.route('/logins')
def logins():
	data={}
	u=request.args['username']
	p=request.args['password']
	q1="select * from login where username='%s' and `password`='%s'"%(u,p)
	print(q1)
	res=select(q1)
	if res:
		data['data']=res
		data['status']='success'
	else:
		data['status']='failed'
	return str(data)

@api.route('/userregister')
def userregister():
	data={}
	f=request.args['fname']
	l=request.args['lname']
	
	pl=request.args['place']
	
	ph=request.args['phone']
	e=request.args['email']
	dis=request.args['district']
	dob=request.args['dob']
	
	u=request.args['username']
	p=request.args['password']
	q="select * from login where username='%s' and password='%s'"%(u,p)
	res=select(q)
	if res:
		data['status']='already'
	else:
		q="insert into login values(NULL,'%s','%s','user')"%(u,p)
		lid=insert(q)
		r="insert into user values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,f,l,dob,ph,e,pl,dis)
		insert(r)
		print(r)
		data['status']="success"
	return str(data)

@api.route('/Viewmedicine')
def Viewmedicine():
	data={}
	
	
	q="select * from medicine "
	res=select(q)
	if res:
		data['data']=res
		data['status']='success'
	data['method']="Viewmedicine"
	return str(data)


@api.route('/searchmedicine')
def searchmedicine():
	data={}
	search=request.args['search']+'%'
	
	
	q="select * from medicine  where name like '%s'"%(search)
	res=select(q)
	if res:
		data['data']=res
		data['status']='success'
	data['method']="searchmedicine"
	return str(data)





@api.route('/BookNow')
def BookNow():
	data={}
	
	log_id=request.args['log_id']
	amt=request.args['amt']
	mid=request.args['mid']
	
	q="insert into booking values(null,(select user_id from user where login_id='%s'),'%s','%s',curdate(),'booked')"%(log_id,mid,amt)
	insert(q)
	print(q)
	data['status']="success"
	return str(data)


@api.route('/Makepayment')
def Makepayment():
	data={}
	
	log_id=request.args['login_id']
	amt=request.args['amt']
	bid=request.args['bid']
	mid=request.args['mid']
	
	q="insert into bookingpayment values(null,(select user_id from user where login_id='%s'),'%s','%s',curdate())"%(log_id,bid,amt)
	insert(q)

	q="update stock set stock=stock-1 where medicine_id='%s'"%(mid)
	update(q)
	q="update  booking set status='Paid' where booking_id='%s'"%(bid)
	update(q)  
	print(q)
	data['status']="success"
	return str(data)


@api.route('/Viewbookings')
def Viewbookings():
	data={}
	
	log_id=request.args['log_id']
	q="select * from booking inner join medicine using (medicine_id) WHERE user_id=(select user_id FROM user where login_id='%s') "%(log_id)
	res=select(q)
	if res:
		data['data']=res
		data['status']='success'
	data['method']="Viewbookings"
	return str(data)