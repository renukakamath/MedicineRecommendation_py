from public import *
import qrcode

pharmacy=Blueprint('pharmacy',__name__)

@pharmacy.route('/pharmacy_home')
def pharmacy_home():
	if not session.get('lid') is None:
		return render_template('pharmacy_home.html')
	else:
		return redirect(url_for('public.login'))


# @pharmacy.route('/phy_view_medicine')
# def phy_view_medicine():
# 	data={}
# 	with open(compiled_contract_path) as file:
# 		contract_json = json.load(file)  # load contract info as JSON
# 		contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
# 	contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
# 	blocknumber = web3.eth.get_block_number()
# 	res = []
# 	try:
# 		for i in range(blocknumber, 0, -1):
# 			a = web3.eth.get_transaction_by_block(i, 0)
# 			decoded_input = contract.decode_function_input(a['input'])
# 			print(decoded_input)
# 			if str(decoded_input[0]) == "<Function add_medicine(uint256,uint256,string,string,string,string,string,string,string,string,string)>":
# 				if int(decoded_input[1]['m_id']) == int(session['lid']):
# 					res.append(decoded_input[1])
# 	except Exception as e:
# 		print("", e)
# 	data['med']=res
# 	return render_template('phy_view_medicine.html',data=data)



@pharmacy.route('/phy_view_manufacture_details',methods=['get','post'])
def phy_view_manufacture_details():
	if not session.get('lid') is None:
		data={}
		with open(compiled_contract_path) as file:
			contract_json = json.load(file)  # load contract info as JSON
			contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
		contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
		blocknumber = web3.eth.get_block_number()
		res = []
		try:
			for i in range(blocknumber, 0, -1):
				a = web3.eth.get_transaction_by_block(i, 0)
				decoded_input = contract.decode_function_input(a['input'])
				print(decoded_input)
				if str(decoded_input[0]) == "<Function add_man(uint256,uint256,string,string,string,string,string,string,string,string,string)>":
					if int(decoded_input[1]['m_id']) == int(session['lid']):
						res.append(decoded_input[1])
		except Exception as e:
			print("", e)
		data['med']=res
		return render_template("phy_view_manufacture_details.html",data=data)
	else:
		return redirect(url_for('public.login'))



@pharmacy.route('/phy_view_medicine',methods=['get','post'])
def phy_view_medicine():
	if not session.get('lid') is None:
		data={}

		# with open(compiled_contract_path) as file:
		# 	contract_json = json.load(file)  # load contract info as JSON
		# 	contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
		# contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
		# blocknumber = web3.eth.get_block_number()
		# res = []
		# try:
		# 	for i in range(blocknumber, 0, -1):
		# 		a = web3.eth.get_transaction_by_block(i, 0)
		# 		decoded_input = contract.decode_function_input(a['input'])
		# 		print("**********************************",decoded_input)
		# 		if str(decoded_input[0]) == "<Function add_medicine(uint256,uint256,string,string,string,string,string,string,string,string)>":
		# 			# if int(decoded_input[1]['m_id']) == int(session['lid']):
		# 			res.append(decoded_input[1])
		# except Exception as e:
		# 	print("", e)
		# data['med']=res
		# print(res)

		with open(compiled_contract_path) as file:
			contract_json = json.load(file)  # load contract info as JSON
			contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
		contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
		blocknumber = web3.eth.get_block_number()
		res = []
		try:
			for i in range(blocknumber, 0, -1):
				a = web3.eth.get_transaction_by_block(i, 0)
				decoded_input = contract.decode_function_input(a['input'])
				print(decoded_input)
				# if str(decoded_input[0]) == "<Function add_medicine(uint256,uint256,string,string,string,string,string,string,string,string)>":
				# 		res.append(decoded_input[1])

				if str(decoded_input[0]) == "<Function add_medicine(uint256,uint256,uint256,string,string,string,string,string,string,string,string,string)>":
					# if int(decoded_input[1]['m_id']) == int(session['lid'])  :
						res.append(decoded_input[1])
		except Exception as e:
			print("", e)

		data['medsss']=res
		print("llllllllllllllllllllllllllllllllllllllllllll",res)

		# if 'action' in request.args:
		# 	action=request.args['action']
		# 	mid=request.args['mid']
		# 	# m_id=request.args['m_id']
		
		# else:
		# 	action=None
			
	# 	if action=="buy":
	# 		q="update stock set pharmacy_id='%s' where medicine_id='%s'"%(session['lid'],mid)

	# 		print(q)
	# 		ids=update(q)

	# 		print(ids)
	# 		q="SELECT * FROM stock INNER JOIN distributor ON `distributor`.`login_id`=`stock`.`distributer_id`  where medicine_id='%s'"%(mid)

	# 		print(q)
	# 		print(q)
	# 		res=select(q)

	# 		stk=res[0]['stock_id']
	# 		print('ggggggggggggggggg',stk)
	# 		with open(compiled_contract_path) as file:
	# 			contract_json = json.load(file)  # load contract info as JSON
	# 			contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions 
	# 		contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
	# 		id=web3.eth.get_block_number()

	# 		message = contract.functions.add_stock(id,int(res[0]['medicine_id']), int(res[0]['manufacture_id']),int(res[0]['distributer_id']), int(res[0]['pharmacy_id']), res[0]['stock'], res[0]['mfg'], res[0]['date']).transact()
			
	# 		# q="select * from stock where stock_id='%s' and medicine_id='%s' and pharmacy_id=(select pharmacy_id from login where login_id='%s')"%(id,mid,session['lid'])
	# 		# print(q)
	# 		# res=select(q)
	# 		# print(res[0]['stock_id'])

	# 		path="static/qrcode/"+str(id)+".png"
	# 		val=qrcode.make(str(id))
	# 		val.save(path)

	# 		q="update stock set QR_code='%s' where stock_id='%s'"%(path,stk)
	# 		print(q)
	# 		update(q)

	# 		flash('picked successfuly')
	# 		return redirect(url_for('pharmacy.phy_view_medicine'))	
		return render_template("phy_view_medicine.html",data=data)
	else:
		return redirect(url_for('public.login'))

@pharmacy.route('/phar_view_stock',methods=['get','post'])
def phar_view_stock():
	if not session.get('lid') is None:
		print("pharmay view stock:::::::::")
		data={}
		mid=request.args['mid']
		amt=request.args['amt']
		data['amt']=amt

		q="select * from stock where medicine_id='%s' "%(mid)
		data['med']=select(q)

		if 'action' in request.args:
			action=request.args['action']
			stockid=request.args['stockid']
			mid=request.args['mid']
			amt=request.args['amt']
			stock=request.args['stock']
			stock_id=request.args['stock_id']

		else:
			action=None
			

		if action=="buy":
			
			return redirect(url_for('pharmacy.phy_make_payment',mid=mid,amt=amt,stock=stock,stock_id=stock_id))	
		return render_template('phar_view_stock.html',data=data)
	else:
		return redirect(url_for('public.login'))


@pharmacy.route('/phy_view_distributer_details',methods=['get','post'])
def phy_view_distributer_details():
	if not session.get('lid') is None:
		data={}
		distributer_id=request.args['distributer_id']
		q="SELECT * FROM `distributor` WHERE `login_id`='%s' "%(distributer_id)
		data['med']=select(q)

		return render_template('phy_view_distributer_details.html',data=data)
	else:
		return redirect(url_for('public.login'))



@pharmacy.route('/phar_send_medicine',methods=['get','post'])
def phar_send_medicine():
	if not session.get('lid') is None:
		data={}
		mid=request.args['mid']
		lid=session['lid']

		q="select * from distributor"
		res=select(q)
		data['dis']=res

		if 'add' in request.form:
			dis=request.form['dis']
			qty=request.form['qty']
			q="insert into request values(null,'%s','%s','0','%s','%s','pending')"%(lid,dis,qty,mid)
			insert(q)
			return redirect(url_for('pharmacy.phar_send_medicine',mid=mid))

		q="select * from request inner join distributor using(distributer_id) where pharmacy_id='%s'"%(lid)
		res=select(q)
		data['med']=res
		return render_template('phar_send_medicine.html',data=data)
	else:
		return redirect(url_for('public.login'))

@pharmacy.route('/phy_make_payment',methods=['get','post'])
def phy_make_payment():
	if not session.get('lid') is None:
		data={}
		lid=session['lid']
		request_id=request.args['request_id']
		# amt=request.args['amt']
		qty=request.args['qty']
		# stock_id=request.args['stock_id']

		# print(amt,qty)

		total_amt=100*int(qty)
		print(total_amt)
		data['total_amt']=total_amt

		if 'payment' in request.form:
			q="insert into payment values(null,'%s','%s','%s',curdate())"%(lid,request_id,total_amt)
			insert(q)
			q="update request set status='Paid' where request_id='%s'"%(request_id)
			update(q)
			return redirect(url_for('pharmacy.pharmacyviewrequest'))
		return render_template('phy_make_payment.html',data=data)
	else:
		return redirect(url_for('public.login'))


@pharmacy.route('/pharmacyviewrequest',methods=['get','post'])
def pharmacyviewrequest():
	if not session.get('lid') is None:
		data={}
		q="SELECT * FROM `request` WHERE `pharmacy_id`='%s' "%(session['lid'])
		data['med']=select(q)

		return render_template('pharmacyviewrequest.html',data=data)
	else:
		return redirect(url_for('public.login'))