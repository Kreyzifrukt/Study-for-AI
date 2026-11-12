namespace HR_App
{
    partial class DepFieId
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(DepFieId));
            groupBox1 = new GroupBox();
            EmpsList = new ListBox();
            DelDepBtn = new Button();
            AddDepBtn = new Button();
            DepField = new TextBox();
            DepsCombo = new ComboBox();
            groupBox2 = new GroupBox();
            DelPhotoBtn = new Button();
            PhotoPanel = new PictureBox();
            AddPhotoBtn = new Button();
            groupBox3 = new GroupBox();
            BirthField = new TextBox();
            DelEmpBtn = new Button();
            PosField = new TextBox();
            AddEmpBtn = new Button();
            label5 = new Label();
            PhoneField = new TextBox();
            Exp = new Label();
            EmailField = new TextBox();
            label3 = new Label();
            label2 = new Label();
            NameField = new TextBox();
            label1 = new Label();
            groupBox1.SuspendLayout();
            groupBox2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)PhotoPanel).BeginInit();
            groupBox3.SuspendLayout();
            SuspendLayout();
            // 
            // groupBox1
            // 
            groupBox1.Controls.Add(EmpsList);
            groupBox1.Controls.Add(DelDepBtn);
            groupBox1.Controls.Add(AddDepBtn);
            groupBox1.Controls.Add(DepField);
            groupBox1.Controls.Add(DepsCombo);
            groupBox1.Location = new Point(12, 12);
            groupBox1.Name = "groupBox1";
            groupBox1.Size = new Size(225, 407);
            groupBox1.TabIndex = 0;
            groupBox1.TabStop = false;
            groupBox1.Text = "Співробітники";
            // 
            // EmpsList
            // 
            EmpsList.FormattingEnabled = true;
            EmpsList.ItemHeight = 19;
            EmpsList.Location = new Point(6, 149);
            EmpsList.Name = "EmpsList";
            EmpsList.Size = new Size(213, 251);
            EmpsList.TabIndex = 4;
            EmpsList.SelectedIndexChanged += EmpsList_SelectedIndexChanged;
            // 
            // DelDepBtn
            // 
            DelDepBtn.Location = new Point(117, 104);
            DelDepBtn.Name = "DelDepBtn";
            DelDepBtn.Size = new Size(102, 37);
            DelDepBtn.TabIndex = 3;
            DelDepBtn.Text = "Видалити";
            DelDepBtn.UseVisualStyleBackColor = true;
            // 
            // AddDepBtn
            // 
            AddDepBtn.Location = new Point(6, 104);
            AddDepBtn.Name = "AddDepBtn";
            AddDepBtn.Size = new Size(102, 37);
            AddDepBtn.TabIndex = 2;
            AddDepBtn.Text = "Додати";
            AddDepBtn.UseVisualStyleBackColor = true;
            AddDepBtn.Click += AddDepBtn_Click;
            // 
            // DepField
            // 
            DepField.Location = new Point(6, 67);
            DepField.Name = "DepField";
            DepField.Size = new Size(213, 26);
            DepField.TabIndex = 1;
            // 
            // DepsCombo
            // 
            DepsCombo.DropDownStyle = ComboBoxStyle.DropDownList;
            DepsCombo.FormattingEnabled = true;
            DepsCombo.Location = new Point(6, 29);
            DepsCombo.Name = "DepsCombo";
            DepsCombo.Size = new Size(213, 27);
            DepsCombo.TabIndex = 0;
            DepsCombo.SelectedIndexChanged += DepsCombo_SelectedIndexChanged;
            // 
            // groupBox2
            // 
            groupBox2.Controls.Add(DelPhotoBtn);
            groupBox2.Controls.Add(PhotoPanel);
            groupBox2.Controls.Add(AddPhotoBtn);
            groupBox2.Location = new Point(243, 12);
            groupBox2.Name = "groupBox2";
            groupBox2.Size = new Size(225, 407);
            groupBox2.TabIndex = 1;
            groupBox2.TabStop = false;
            groupBox2.Text = "Фото";
            // 
            // DelPhotoBtn
            // 
            DelPhotoBtn.Location = new Point(117, 361);
            DelPhotoBtn.Name = "DelPhotoBtn";
            DelPhotoBtn.Size = new Size(102, 37);
            DelPhotoBtn.TabIndex = 6;
            DelPhotoBtn.Text = "Видалити";
            DelPhotoBtn.UseVisualStyleBackColor = true;
            // 
            // PhotoPanel
            // 
            PhotoPanel.Image = (Image)resources.GetObject("PhotoPanel.Image");
            PhotoPanel.Location = new Point(6, 29);
            PhotoPanel.Name = "PhotoPanel";
            PhotoPanel.Size = new Size(213, 321);
            PhotoPanel.SizeMode = PictureBoxSizeMode.Zoom;
            PhotoPanel.TabIndex = 0;
            PhotoPanel.TabStop = false;
            // 
            // AddPhotoBtn
            // 
            AddPhotoBtn.Location = new Point(6, 361);
            AddPhotoBtn.Name = "AddPhotoBtn";
            AddPhotoBtn.Size = new Size(102, 37);
            AddPhotoBtn.TabIndex = 5;
            AddPhotoBtn.Text = "Додати";
            AddPhotoBtn.UseVisualStyleBackColor = true;
            // 
            // groupBox3
            // 
            groupBox3.Controls.Add(BirthField);
            groupBox3.Controls.Add(DelEmpBtn);
            groupBox3.Controls.Add(PosField);
            groupBox3.Controls.Add(AddEmpBtn);
            groupBox3.Controls.Add(label5);
            groupBox3.Controls.Add(PhoneField);
            groupBox3.Controls.Add(Exp);
            groupBox3.Controls.Add(EmailField);
            groupBox3.Controls.Add(label3);
            groupBox3.Controls.Add(label2);
            groupBox3.Controls.Add(NameField);
            groupBox3.Controls.Add(label1);
            groupBox3.Location = new Point(474, 12);
            groupBox3.Name = "groupBox3";
            groupBox3.Size = new Size(225, 407);
            groupBox3.TabIndex = 1;
            groupBox3.TabStop = false;
            groupBox3.Text = "Персональні дані";
            // 
            // BirthField
            // 
            BirthField.Location = new Point(8, 115);
            BirthField.Name = "BirthField";
            BirthField.Size = new Size(191, 26);
            BirthField.TabIndex = 14;
            // 
            // DelEmpBtn
            // 
            DelEmpBtn.Location = new Point(117, 361);
            DelEmpBtn.Name = "DelEmpBtn";
            DelEmpBtn.Size = new Size(102, 37);
            DelEmpBtn.TabIndex = 8;
            DelEmpBtn.Text = "Видалити";
            DelEmpBtn.UseVisualStyleBackColor = true;
            // 
            // PosField
            // 
            PosField.Location = new Point(6, 299);
            PosField.Name = "PosField";
            PosField.Size = new Size(213, 26);
            PosField.TabIndex = 13;
            // 
            // AddEmpBtn
            // 
            AddEmpBtn.Location = new Point(6, 361);
            AddEmpBtn.Name = "AddEmpBtn";
            AddEmpBtn.Size = new Size(102, 37);
            AddEmpBtn.TabIndex = 7;
            AddEmpBtn.Text = "Додати";
            AddEmpBtn.UseVisualStyleBackColor = true;
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Location = new Point(6, 273);
            label5.Name = "label5";
            label5.Size = new Size(63, 19);
            label5.TabIndex = 12;
            label5.Text = "Телефон";
            // 
            // PhoneField
            // 
            PhoneField.Location = new Point(6, 238);
            PhoneField.Name = "PhoneField";
            PhoneField.Size = new Size(213, 26);
            PhoneField.TabIndex = 11;
            // 
            // Exp
            // 
            Exp.AutoSize = true;
            Exp.Location = new Point(6, 212);
            Exp.Name = "Exp";
            Exp.Size = new Size(41, 19);
            Exp.TabIndex = 10;
            Exp.Text = "Стаж";
            // 
            // EmailField
            // 
            EmailField.Location = new Point(6, 177);
            EmailField.Name = "EmailField";
            EmailField.Size = new Size(213, 26);
            EmailField.TabIndex = 9;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(6, 151);
            label3.Name = "label3";
            label3.Size = new Size(129, 19);
            label3.TabIndex = 8;
            label3.Text = "Електронна пошта:";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(6, 90);
            label2.Name = "label2";
            label2.Size = new Size(110, 19);
            label2.TabIndex = 6;
            label2.Text = "Рік народження";
            // 
            // NameField
            // 
            NameField.Location = new Point(6, 55);
            NameField.Name = "NameField";
            NameField.Size = new Size(213, 26);
            NameField.TabIndex = 5;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(6, 29);
            label1.Name = "label1";
            label1.Size = new Size(117, 19);
            label1.TabIndex = 0;
            label1.Text = "Прізвище та ім'я:";
            // 
            // DepFieId
            // 
            AutoScaleDimensions = new SizeF(8F, 19F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(709, 427);
            Controls.Add(groupBox3);
            Controls.Add(groupBox2);
            Controls.Add(groupBox1);
            Font = new Font("Segoe UI", 10.2F, FontStyle.Regular, GraphicsUnit.Point, 204);
            FormBorderStyle = FormBorderStyle.Fixed3D;
            MaximizeBox = false;
            Name = "DepFieId";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "Відділ кадрів";
            Load += Form1_Load;
            groupBox1.ResumeLayout(false);
            groupBox1.PerformLayout();
            groupBox2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)PhotoPanel).EndInit();
            groupBox3.ResumeLayout(false);
            groupBox3.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private GroupBox groupBox1;
        private GroupBox groupBox2;
        private GroupBox groupBox3;
        private ComboBox DepsCombo;
        private Button DelDepBtn;
        private Button AddDepBtn;
        private TextBox DepField;
        private ListBox EmpsList;
        private Button DelPhotoBtn;
        private PictureBox PhotoPanel;
        private Button AddPhotoBtn;
        private Label label1;
        private Button DelEmpBtn;
        private TextBox PosField;
        private Button AddEmpBtn;
        private Label label5;
        private TextBox PhoneField;
        private Label Exp;
        private TextBox EmailField;
        private Label label3;
        private Label label2;
        private TextBox NameField;
        private TextBox BirthField;
    }
}
