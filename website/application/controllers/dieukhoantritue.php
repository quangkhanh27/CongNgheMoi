<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class dieukhoantritue extends CI_Controller {
	// Hàm khởi tạo
    function __construct() {
        parent::__construct();
        $this->data['com']='dieukhoantritue';
        $this->load->model('frontend/Mcategory');
    }
    
	public function index(){
        $this->data['title']='24hStore.vn - Điều khoản';
        $this->data['view']='index';
		$this->load->view('frontend/layout',$this->data);
	}
}
