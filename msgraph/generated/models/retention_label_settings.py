from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .security import behavior_during_retention_period

class RetentionLabelSettings(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new retentionLabelSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The behaviorDuringRetentionPeriod property
        self._behavior_during_retention_period: Optional[behavior_during_retention_period.BehaviorDuringRetentionPeriod] = None
        # The isContentUpdateAllowed property
        self._is_content_update_allowed: Optional[bool] = None
        # The isDeleteAllowed property
        self._is_delete_allowed: Optional[bool] = None
        # The isLabelUpdateAllowed property
        self._is_label_update_allowed: Optional[bool] = None
        # The isMetadataUpdateAllowed property
        self._is_metadata_update_allowed: Optional[bool] = None
        # The isRecordLocked property
        self._is_record_locked: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    def behavior_during_retention_period(self,) -> Optional[behavior_during_retention_period.BehaviorDuringRetentionPeriod]:
        """
        Gets the behaviorDuringRetentionPeriod property value. The behaviorDuringRetentionPeriod property
        Returns: Optional[behavior_during_retention_period.BehaviorDuringRetentionPeriod]
        """
        return self._behavior_during_retention_period
    
    @behavior_during_retention_period.setter
    def behavior_during_retention_period(self,value: Optional[behavior_during_retention_period.BehaviorDuringRetentionPeriod] = None) -> None:
        """
        Sets the behaviorDuringRetentionPeriod property value. The behaviorDuringRetentionPeriod property
        Args:
            value: Value to set for the behavior_during_retention_period property.
        """
        self._behavior_during_retention_period = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RetentionLabelSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RetentionLabelSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RetentionLabelSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .security import behavior_during_retention_period

        fields: Dict[str, Callable[[Any], None]] = {
            "behaviorDuringRetentionPeriod": lambda n : setattr(self, 'behavior_during_retention_period', n.get_enum_value(behavior_during_retention_period.BehaviorDuringRetentionPeriod)),
            "isContentUpdateAllowed": lambda n : setattr(self, 'is_content_update_allowed', n.get_bool_value()),
            "isDeleteAllowed": lambda n : setattr(self, 'is_delete_allowed', n.get_bool_value()),
            "isLabelUpdateAllowed": lambda n : setattr(self, 'is_label_update_allowed', n.get_bool_value()),
            "isMetadataUpdateAllowed": lambda n : setattr(self, 'is_metadata_update_allowed', n.get_bool_value()),
            "isRecordLocked": lambda n : setattr(self, 'is_record_locked', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_content_update_allowed(self,) -> Optional[bool]:
        """
        Gets the isContentUpdateAllowed property value. The isContentUpdateAllowed property
        Returns: Optional[bool]
        """
        return self._is_content_update_allowed
    
    @is_content_update_allowed.setter
    def is_content_update_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the isContentUpdateAllowed property value. The isContentUpdateAllowed property
        Args:
            value: Value to set for the is_content_update_allowed property.
        """
        self._is_content_update_allowed = value
    
    @property
    def is_delete_allowed(self,) -> Optional[bool]:
        """
        Gets the isDeleteAllowed property value. The isDeleteAllowed property
        Returns: Optional[bool]
        """
        return self._is_delete_allowed
    
    @is_delete_allowed.setter
    def is_delete_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDeleteAllowed property value. The isDeleteAllowed property
        Args:
            value: Value to set for the is_delete_allowed property.
        """
        self._is_delete_allowed = value
    
    @property
    def is_label_update_allowed(self,) -> Optional[bool]:
        """
        Gets the isLabelUpdateAllowed property value. The isLabelUpdateAllowed property
        Returns: Optional[bool]
        """
        return self._is_label_update_allowed
    
    @is_label_update_allowed.setter
    def is_label_update_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the isLabelUpdateAllowed property value. The isLabelUpdateAllowed property
        Args:
            value: Value to set for the is_label_update_allowed property.
        """
        self._is_label_update_allowed = value
    
    @property
    def is_metadata_update_allowed(self,) -> Optional[bool]:
        """
        Gets the isMetadataUpdateAllowed property value. The isMetadataUpdateAllowed property
        Returns: Optional[bool]
        """
        return self._is_metadata_update_allowed
    
    @is_metadata_update_allowed.setter
    def is_metadata_update_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMetadataUpdateAllowed property value. The isMetadataUpdateAllowed property
        Args:
            value: Value to set for the is_metadata_update_allowed property.
        """
        self._is_metadata_update_allowed = value
    
    @property
    def is_record_locked(self,) -> Optional[bool]:
        """
        Gets the isRecordLocked property value. The isRecordLocked property
        Returns: Optional[bool]
        """
        return self._is_record_locked
    
    @is_record_locked.setter
    def is_record_locked(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRecordLocked property value. The isRecordLocked property
        Args:
            value: Value to set for the is_record_locked property.
        """
        self._is_record_locked = value
    
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("behaviorDuringRetentionPeriod", self.behavior_during_retention_period)
        writer.write_bool_value("isContentUpdateAllowed", self.is_content_update_allowed)
        writer.write_bool_value("isDeleteAllowed", self.is_delete_allowed)
        writer.write_bool_value("isLabelUpdateAllowed", self.is_label_update_allowed)
        writer.write_bool_value("isMetadataUpdateAllowed", self.is_metadata_update_allowed)
        writer.write_bool_value("isRecordLocked", self.is_record_locked)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

