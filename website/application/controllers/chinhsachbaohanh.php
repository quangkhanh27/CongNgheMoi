<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class chinhsachbaohanh extends CI_Controller {
	// Hàm khởi tạo
    function __construct() {
        parent::__construct();
        $this->data['com']='chinhsachbaohanh';
        $this->load->model('frontend/Mcategory');
    }
    
	public function index(){
        $this->data['title']='24hStore.vn - Chính sách';
        $this->data['view']='index';
		$this->load->view('frontend/layout',$this->data);
	}
}
