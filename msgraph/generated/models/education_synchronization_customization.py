from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class EducationSynchronizationCustomization(AdditionalDataHolder, Parsable):
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
    def allow_display_name_update(self,) -> Optional[bool]:
        """
        Gets the allowDisplayNameUpdate property value. Indicates whether the display name of the resource can be overwritten by the sync.
        Returns: Optional[bool]
        """
        return self._allow_display_name_update
    
    @allow_display_name_update.setter
    def allow_display_name_update(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowDisplayNameUpdate property value. Indicates whether the display name of the resource can be overwritten by the sync.
        Args:
            value: Value to set for the allowDisplayNameUpdate property.
        """
        self._allow_display_name_update = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new educationSynchronizationCustomization and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether the display name of the resource can be overwritten by the sync.
        self._allow_display_name_update: Optional[bool] = None
        # Indicates whether synchronization of the parent entity is deferred to a later date.
        self._is_sync_deferred: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The collection of property names to sync. If set to null, all properties will be synchronized. Does not apply to Student Enrollments or Teacher Rosters
        self._optional_properties_to_sync: Optional[List[str]] = None
        # The date that the synchronization should start. This value should be set to a future date. If set to null, the resource will be synchronized when the profile setup completes. Only applies to Student Enrollments
        self._synchronization_start_date: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationSynchronizationCustomization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationSynchronizationCustomization
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationSynchronizationCustomization()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_display_name_update": lambda n : setattr(self, 'allow_display_name_update', n.get_bool_value()),
            "is_sync_deferred": lambda n : setattr(self, 'is_sync_deferred', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "optional_properties_to_sync": lambda n : setattr(self, 'optional_properties_to_sync', n.get_collection_of_primitive_values(str)),
            "synchronization_start_date": lambda n : setattr(self, 'synchronization_start_date', n.get_datetime_value()),
        }
        return fields
    
    @property
    def is_sync_deferred(self,) -> Optional[bool]:
        """
        Gets the isSyncDeferred property value. Indicates whether synchronization of the parent entity is deferred to a later date.
        Returns: Optional[bool]
        """
        return self._is_sync_deferred
    
    @is_sync_deferred.setter
    def is_sync_deferred(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSyncDeferred property value. Indicates whether synchronization of the parent entity is deferred to a later date.
        Args:
            value: Value to set for the isSyncDeferred property.
        """
        self._is_sync_deferred = value
    
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
    def optional_properties_to_sync(self,) -> Optional[List[str]]:
        """
        Gets the optionalPropertiesToSync property value. The collection of property names to sync. If set to null, all properties will be synchronized. Does not apply to Student Enrollments or Teacher Rosters
        Returns: Optional[List[str]]
        """
        return self._optional_properties_to_sync
    
    @optional_properties_to_sync.setter
    def optional_properties_to_sync(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the optionalPropertiesToSync property value. The collection of property names to sync. If set to null, all properties will be synchronized. Does not apply to Student Enrollments or Teacher Rosters
        Args:
            value: Value to set for the optionalPropertiesToSync property.
        """
        self._optional_properties_to_sync = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("allowDisplayNameUpdate", self.allow_display_name_update)
        writer.write_bool_value("isSyncDeferred", self.is_sync_deferred)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("optionalPropertiesToSync", self.optional_properties_to_sync)
        writer.write_datetime_value("synchronizationStartDate", self.synchronization_start_date)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def synchronization_start_date(self,) -> Optional[datetime]:
        """
        Gets the synchronizationStartDate property value. The date that the synchronization should start. This value should be set to a future date. If set to null, the resource will be synchronized when the profile setup completes. Only applies to Student Enrollments
        Returns: Optional[datetime]
        """
        return self._synchronization_start_date
    
    @synchronization_start_date.setter
    def synchronization_start_date(self,value: Optional[datetime] = None) -> None:
        """
        Sets the synchronizationStartDate property value. The date that the synchronization should start. This value should be set to a future date. If set to null, the resource will be synchronized when the profile setup completes. Only applies to Student Enrollments
        Args:
            value: Value to set for the synchronizationStartDate property.
        """
        self._synchronization_start_date = value
    

