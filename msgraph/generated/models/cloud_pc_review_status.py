from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_pc_user_access_level = lazy_import('msgraph.generated.models.cloud_pc_user_access_level')

class CloudPcReviewStatus(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def azure_storage_account_id(self,) -> Optional[str]:
        """
        Gets the azureStorageAccountId property value. The resource ID of the Azure Storage account in which the Cloud PC snapshot is being saved.
        Returns: Optional[str]
        """
        return self._azure_storage_account_id
    
    @azure_storage_account_id.setter
    def azure_storage_account_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureStorageAccountId property value. The resource ID of the Azure Storage account in which the Cloud PC snapshot is being saved.
        Args:
            value: Value to set for the azureStorageAccountId property.
        """
        self._azure_storage_account_id = value
    
    @property
    def azure_storage_account_name(self,) -> Optional[str]:
        """
        Gets the azureStorageAccountName property value. The name of the Azure Storage account in which the Cloud PC snapshot is being saved.
        Returns: Optional[str]
        """
        return self._azure_storage_account_name
    
    @azure_storage_account_name.setter
    def azure_storage_account_name(self,value: Optional[str] = None) -> None:
        """
        Sets the azureStorageAccountName property value. The name of the Azure Storage account in which the Cloud PC snapshot is being saved.
        Args:
            value: Value to set for the azureStorageAccountName property.
        """
        self._azure_storage_account_name = value
    
    @property
    def azure_storage_container_name(self,) -> Optional[str]:
        """
        Gets the azureStorageContainerName property value. The name of the container in an Azure Storage account in which the Cloud PC snapshot is being saved.
        Returns: Optional[str]
        """
        return self._azure_storage_container_name
    
    @azure_storage_container_name.setter
    def azure_storage_container_name(self,value: Optional[str] = None) -> None:
        """
        Sets the azureStorageContainerName property value. The name of the container in an Azure Storage account in which the Cloud PC snapshot is being saved.
        Args:
            value: Value to set for the azureStorageContainerName property.
        """
        self._azure_storage_container_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new cloudPcReviewStatus and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The resource ID of the Azure Storage account in which the Cloud PC snapshot is being saved.
        self._azure_storage_account_id: Optional[str] = None
        # The name of the Azure Storage account in which the Cloud PC snapshot is being saved.
        self._azure_storage_account_name: Optional[str] = None
        # The name of the container in an Azure Storage account in which the Cloud PC snapshot is being saved.
        self._azure_storage_container_name: Optional[str] = None
        # True if the Cloud PC is set to in review by the administrator.
        self._in_review: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The specific date and time of the Cloud PC snapshot that was taken and saved automatically, when the Cloud PC is set to in review. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as 2014-01-01T00:00:00Z.
        self._restore_point_date_time: Optional[datetime] = None
        # The specific date and time when the Cloud PC was set to in review. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as 2014-01-01T00:00:00Z.
        self._review_start_date_time: Optional[datetime] = None
        # The ID of the Azure subscription in which the Cloud PC snapshot is being saved, in GUID format.
        self._subscription_id: Optional[str] = None
        # The name of the Azure subscription in which the Cloud PC snapshot is being saved.
        self._subscription_name: Optional[str] = None
        # The userAccessLevel property
        self._user_access_level: Optional[cloud_pc_user_access_level.CloudPcUserAccessLevel] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcReviewStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcReviewStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcReviewStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "azure_storage_account_id": lambda n : setattr(self, 'azure_storage_account_id', n.get_str_value()),
            "azure_storage_account_name": lambda n : setattr(self, 'azure_storage_account_name', n.get_str_value()),
            "azure_storage_container_name": lambda n : setattr(self, 'azure_storage_container_name', n.get_str_value()),
            "in_review": lambda n : setattr(self, 'in_review', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "restore_point_date_time": lambda n : setattr(self, 'restore_point_date_time', n.get_datetime_value()),
            "review_start_date_time": lambda n : setattr(self, 'review_start_date_time', n.get_datetime_value()),
            "subscription_id": lambda n : setattr(self, 'subscription_id', n.get_str_value()),
            "subscription_name": lambda n : setattr(self, 'subscription_name', n.get_str_value()),
            "user_access_level": lambda n : setattr(self, 'user_access_level', n.get_enum_value(cloud_pc_user_access_level.CloudPcUserAccessLevel)),
        }
        return fields
    
    @property
    def in_review(self,) -> Optional[bool]:
        """
        Gets the inReview property value. True if the Cloud PC is set to in review by the administrator.
        Returns: Optional[bool]
        """
        return self._in_review
    
    @in_review.setter
    def in_review(self,value: Optional[bool] = None) -> None:
        """
        Sets the inReview property value. True if the Cloud PC is set to in review by the administrator.
        Args:
            value: Value to set for the inReview property.
        """
        self._in_review = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def restore_point_date_time(self,) -> Optional[datetime]:
        """
        Gets the restorePointDateTime property value. The specific date and time of the Cloud PC snapshot that was taken and saved automatically, when the Cloud PC is set to in review. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._restore_point_date_time
    
    @restore_point_date_time.setter
    def restore_point_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the restorePointDateTime property value. The specific date and time of the Cloud PC snapshot that was taken and saved automatically, when the Cloud PC is set to in review. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the restorePointDateTime property.
        """
        self._restore_point_date_time = value
    
    @property
    def review_start_date_time(self,) -> Optional[datetime]:
        """
        Gets the reviewStartDateTime property value. The specific date and time when the Cloud PC was set to in review. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._review_start_date_time
    
    @review_start_date_time.setter
    def review_start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the reviewStartDateTime property value. The specific date and time when the Cloud PC was set to in review. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the reviewStartDateTime property.
        """
        self._review_start_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("azureStorageAccountId", self.azure_storage_account_id)
        writer.write_str_value("azureStorageAccountName", self.azure_storage_account_name)
        writer.write_str_value("azureStorageContainerName", self.azure_storage_container_name)
        writer.write_bool_value("inReview", self.in_review)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("restorePointDateTime", self.restore_point_date_time)
        writer.write_datetime_value("reviewStartDateTime", self.review_start_date_time)
        writer.write_str_value("subscriptionId", self.subscription_id)
        writer.write_str_value("subscriptionName", self.subscription_name)
        writer.write_enum_value("userAccessLevel", self.user_access_level)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def subscription_id(self,) -> Optional[str]:
        """
        Gets the subscriptionId property value. The ID of the Azure subscription in which the Cloud PC snapshot is being saved, in GUID format.
        Returns: Optional[str]
        """
        return self._subscription_id
    
    @subscription_id.setter
    def subscription_id(self,value: Optional[str] = None) -> None:
        """
        Sets the subscriptionId property value. The ID of the Azure subscription in which the Cloud PC snapshot is being saved, in GUID format.
        Args:
            value: Value to set for the subscriptionId property.
        """
        self._subscription_id = value
    
    @property
    def subscription_name(self,) -> Optional[str]:
        """
        Gets the subscriptionName property value. The name of the Azure subscription in which the Cloud PC snapshot is being saved.
        Returns: Optional[str]
        """
        return self._subscription_name
    
    @subscription_name.setter
    def subscription_name(self,value: Optional[str] = None) -> None:
        """
        Sets the subscriptionName property value. The name of the Azure subscription in which the Cloud PC snapshot is being saved.
        Args:
            value: Value to set for the subscriptionName property.
        """
        self._subscription_name = value
    
    @property
    def user_access_level(self,) -> Optional[cloud_pc_user_access_level.CloudPcUserAccessLevel]:
        """
        Gets the userAccessLevel property value. The userAccessLevel property
        Returns: Optional[cloud_pc_user_access_level.CloudPcUserAccessLevel]
        """
        return self._user_access_level
    
    @user_access_level.setter
    def user_access_level(self,value: Optional[cloud_pc_user_access_level.CloudPcUserAccessLevel] = None) -> None:
        """
        Sets the userAccessLevel property value. The userAccessLevel property
        Args:
            value: Value to set for the userAccessLevel property.
        """
        self._user_access_level = value
    

