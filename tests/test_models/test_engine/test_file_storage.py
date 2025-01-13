
            os.remove(self.test_file)

    def test_all_storage_returns_dictionary(self):
        """
        Test if the all() method returns a dictionary.
        """
        self.assertEqual({}, models.storage.all())

    def test_new(self):
        """
        Test that the new() method adds a new object to the storage dictionary.
        """
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn(f"BaseModel.{obj.id}", models.storage.all())

    def test_new_with_args(self):
        """Test that the new() method raises TypeError when given additional
        arguments."""       
        self.assertRaises(TypeError, models.storage.new, 1)

    def test_new_with_none(self):
        """
        Test that creating a new object with None raises AttributeError. This
        ensures that the new() method does not allow None as an argument.
        """
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_and_reload(self):
        """
        Test that the save() method saves objects to a file and then reloads
        them back into the storage dictionary when the reload() method is
        called.
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        models.storage.new(obj1)
        models.storage.new(obj2)
        models.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        # Check if the reloaded objects match the original objects
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj1.id)) is not None)
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj2.id)) is not None)

    def test_save_to_file(self):
        """
        Test saving objects to a file and check if the file is created.
        """
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

    def test_reload_empty_file(self):
        """
        Test that the reload() method raises TypeError when the file is empty or does not exist
        """
        with self.assertRaises(TypeError):
            models.storage.reload()

if __name__ == "__main__":
    unittest.main()
