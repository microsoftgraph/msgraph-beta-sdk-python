from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_user_access_level import CloudPcUserAccessLevel

@dataclass
class CloudPcReviewStatus(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The resource ID of the Azure Storage account in which the Cloud PC snapshot is being saved.
    azure_storage_account_id: Optional[str] = None
    # The name of the Azure Storage account in which the Cloud PC snapshot is being saved.
    azure_storage_account_name: Optional[str] = None
    # The name of the container in an Azure Storage account in which the Cloud PC snapshot is being saved.
    azure_storage_container_name: Optional[str] = None
    # True if the Cloud PC is set to in review by the administrator.
    in_review: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The specific date and time of the Cloud PC snapshot that was taken and saved automatically, when the Cloud PC is set to in review. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as 2014-01-01T00:00:00Z.
    restore_point_date_time: Optional[datetime.datetime] = None
    # The specific date and time when the Cloud PC was set to in review. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as 2014-01-01T00:00:00Z.
    review_start_date_time: Optional[datetime.datetime] = None
    # The ID of the Azure subscription in which the Cloud PC snapshot is being saved, in GUID format.
    subscription_id: Optional[str] = None
    # The name of the Azure subscription in which the Cloud PC snapshot is being saved.
    subscription_name: Optional[str] = None
    # The userAccessLevel property
    user_access_level: Optional[CloudPcUserAccessLevel] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcReviewStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcReviewStatus
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudPcReviewStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_user_access_level import CloudPcUserAccessLevel

        from .cloud_pc_user_access_level import CloudPcUserAccessLevel

        fields: Dict[str, Callable[[Any], None]] = {
            "azureStorageAccountId": lambda n : setattr(self, 'azure_storage_account_id', n.get_str_value()),
            "azureStorageAccountName": lambda n : setattr(self, 'azure_storage_account_name', n.get_str_value()),
            "azureStorageContainerName": lambda n : setattr(self, 'azure_storage_container_name', n.get_str_value()),
            "inReview": lambda n : setattr(self, 'in_review', n.get_bool_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "restorePointDateTime": lambda n : setattr(self, 'restore_point_date_time', n.get_datetime_value()),
            "reviewStartDateTime": lambda n : setattr(self, 'review_start_date_time', n.get_datetime_value()),
            "subscriptionId": lambda n : setattr(self, 'subscription_id', n.get_str_value()),
            "subscriptionName": lambda n : setattr(self, 'subscription_name', n.get_str_value()),
            "userAccessLevel": lambda n : setattr(self, 'user_access_level', n.get_enum_value(CloudPcUserAccessLevel)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("azureStorageAccountId", self.azure_storage_account_id)
        writer.write_str_value("azureStorageAccountName", self.azure_storage_account_name)
        writer.write_str_value("azureStorageContainerName", self.azure_storage_container_name)
        writer.write_bool_value("inReview", self.in_review)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_datetime_value("restorePointDateTime", self.restore_point_date_time)
        writer.write_datetime_value("reviewStartDateTime", self.review_start_date_time)
        writer.write_str_value("subscriptionId", self.subscription_id)
        writer.write_str_value("subscriptionName", self.subscription_name)
        writer.write_enum_value("userAccessLevel", self.user_access_level)
        writer.write_additional_data_value(self.additional_data)
    

