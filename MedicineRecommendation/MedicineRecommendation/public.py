import datetime
from flask import *
from database import *
import uuid
import json
from web3 import Web3, HTTPProvider

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:9545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]
compiled_contract_path = 'C:/Users/DELL/Desktop/MedicineRecommendation/MedicineRecommendation/MedicineRecommendation/node_modules/.bin/build/contracts/medicines.json'
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0x7D76E0a7531390ddF6D509Dcb94bd39cAaBD0a2D'
# syspath=r"C:\Users\DELL\Desktop\MedicineRecommendation\MedicineRecommendation\MedicineRecommendation\static\\"
syspath=r"C:\Users\DELL\Desktop\MedicineRecommendation\MedicineRecommendation\MedicineRecommendation\static\\"

public=Blueprint('public',__name__)

@public.route('/')
def home():
	session.clear()
	return render_template('home.html')

@public.route('/login',methods=['get','post'])
def login():
	session.clear()
	if 'submit' in request.form:
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="SELECT * FROM `login` WHERE `username`='%s' AND `password`='%s'"%(uname,pwd)
		res=select(q)
		if res:
			session['lid']=res[0]['login_id']


			if res[0]['usertype']=='admin':
				flash("login successfully....!")
				return redirect(url_for('admin.admin_home'))
			elif res[0]['usertype']=='manufacturer':
				flash("login successfully....!")
				return redirect(url_for('manufacturer.manufacturer_home'))
			elif res[0]['usertype']=='distributor':
				flash("login successfully....!")
				return redirect(url_for('distributor.distributor_home'))
			elif res[0]['usertype']=='pharmacy':
				flash("login successfully....!")
				return redirect(url_for('pharmacy.pharmacy_home'))			
			elif res[0]['usertype']=='pending':
				flash("!!!!.....your account is on proccessing.....!!!!")

		
	
		else:

			flash("INVALID USERNAME OR PASSWORD")
	return render_template('login.html')


@public.route('/customer_register',methods=['get','post'])
def customer_register():
	if 'submit' in request.form:
		fname=request.form['fn']
		place=request.form['pl']
		phone=request.form['ph']
		email=request.form['em']
		i=request.files['i']
		dis=request.form['dis']
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="select * from login where username='%s' and password='%s'" %(uname,pwd)
		res=select(q)
		if res:
			flash("USERNAME AND PASSWORD IS ALREADY EXIST")
		else:
			
			extn = (i.filename.split('.'))
			d = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
			path = '/static/' + d + '.' + str(extn[-1])
			i.save(syspath + d + '.' + str(extn[-1]))

			q="INSERT INTO `login` VALUES(null,'%s','%s','pending')"%(uname,pwd)
			id=insert(q)
			q1="INSERT INTO `manufacture` VALUES(null,'%s','%s','%s','%s','%s','%s','%s')"%(id,fname,phone,email,place,dis,path)
			insert(q1)

			# z="insert into product values(null,'%s','%s','%s','%s','pending')"%(fid,pro,det,rate)
			# insert(z)
			# add section
			# with open(compiled_contract_path) as file:
			# 	contract_json = json.load(file)  # load contract info as JSON
			# 	contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
			# contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
			# message = contract.functions.add_man(id, fname, place, phone, email,dis,path).transact()
			flash('registered')
		return redirect(url_for('public.customer_register'))
	return render_template("customer_register.html")



@public.route('/pharmacy_register',methods=['get','post'])
def pharmacy_register():
	if 'submit' in request.form:
		pn=request.form['pn']
		city=request.form['city']
		place=request.form['pl']
		phone=request.form['ph']
		email=request.form['em']
		uname=request.form['uname']
		pwd=request.form['pwd']
		i=request.files['i']
		path='static/'+str(uuid.uuid4())+i.filename
		print("dddddddd",path)
		i.save(path)
		q="select * from login where username='%s' and password='%s'" %(uname,pwd)
		res=select(q)
		if res:
			flash("USERNAME AND PASSWORD IS ALREADY EXIST")
		else:
			q="INSERT INTO `login` VALUES(null,'%s','%s','pending')"%(uname,pwd)
			id=insert(q)
			q1="INSERT INTO `pharmacy` VALUES(null,'%s','%s','%s','%s','%s','%s','%s')"%(id,pn,place,city,email,phone,path)
			insert(q1)
			flash('registered')
		return redirect(url_for('public.pharmacy_register'))

	return render_template("pharmacy_register.html")




@public.route('/distributor_register',methods=['get','post'])
def distributor_register():
	if 'submit' in request.form:
		fname=request.form['fn']
		lname=request.form['ln']
		place=request.form['pl']
		phone=request.form['ph']
		email=request.form['em']
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="select * from login where username='%s' and password='%s'" %(uname,pwd)
		res=select(q)
		if res:
			flash("USERNAME AND PASSWORD IS ALREADY EXIST")
		else:
			q="INSERT INTO `login` VALUES(null,'%s','%s','pending')"%(uname,pwd)
			id=insert(q)
			q1="INSERT INTO `distributor` VALUES(null,'%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,phone,email)
			insert(q1)


			flash('registered')
		return redirect(url_for('public.distributor_register'))

	return render_template("distributor_register.html")



@public.route('/customer_view',methods=['get','post'])
def customer_view():
	data={}
	# q="select * from medicine "
	# res=select(q)
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
	# 		print(decoded_input)
	# 		if str(decoded_input[0]) == "<Function add_medicine(uint256,uint256,string,string,string,string,string,string,string,string)>":
	# 				res.append(decoded_input[1])
	# except Exception as e:
	# 	print("", e)

	# data['meddddddddddd']=res

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
			print("***********************************",decoded_input)
			# if str(decoded_input[0]) == "<Function add_medicine(uint256,uint256,string,string,string,string,string,string,string,string)>":
			# 		res.append(decoded_input[1])

			if str(decoded_input[0]) == "<Function add_medicine(uint256,uint256,uint256,string,string,string,string,string,string,string,string,string)>":
				# if int(decoded_input[1]['m_id']) == int(session['lid'])  :
					res.append(decoded_input[1])
	except Exception as e:
		print("", e)

	data['meddddddddddd']=res

	print("kkkkkkkkkkkkkkkkkkk",data['meddddddddddd'])
	# for i in res:
	# 	mname=i['name']
	# 	print("0000000000000000000",mname)

	if 'submit' in request.form:
		sname=request.form['sname']+"%"

		q="select * from  medicine  where name like '%s' "%(sname)
		print("lllllllllllllllllll",q)
		data['meddddddddddd']=select(q)
	else:
		data['meddddddddddd']=res


	return render_template('customer_view.html',data=data)



@public.route('/customer_view_stock',methods=['get','post'])
def customer_view_stock():
	data={}
	mid=request.args['mid']
	q="select * from stock where medicine_id='%s' "%(mid)
	print("/////////////////////////",q)
	data['med']=select(q)

	return render_template('customer_view_stock.html',data=data)

