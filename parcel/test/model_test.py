import pytest


@pytest.mark.django_db
class TestParcel:
    def test_parcel_creation(self, create_parcel_record):
        assert create_parcel_record.id != '', "Should create a parcel instance"

    def test_parcel_str(self, create_parcel_record):
        assert create_parcel_record.__str__() == create_parcel_record.tracking_number, "Should return the tracking " \
                                                                                       "number"

    def test_parcel_update(self, create_parcel_record):
        create_parcel_record.sender = "John Doe"
        create_parcel_record.save()
        assert create_parcel_record.sender == "John Doe", "Should update the sender field"

    def test_parcel_delete(self, create_parcel_record):
        create_parcel_record.delete()
        assert create_parcel_record.id is None, "Should delete the parcel record"
