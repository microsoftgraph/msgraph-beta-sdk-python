from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
public_error = lazy_import('msgraph.generated.models.public_error')
industry_data_activity = lazy_import('msgraph.generated.models.industry_data.industry_data_activity')
industry_data_activity_status = lazy_import('msgraph.generated.models.industry_data.industry_data_activity_status')

class IndustryDataRunActivity(entity.Entity):
    @property
    def activity(self,) -> Optional[industry_data_activity.IndustryDataActivity]:
        """
        Gets the activity property value. The flow that was run by this activity.
        Returns: Optional[industry_data_activity.IndustryDataActivity]
        """
        return self._activity
    
    @activity.setter
    def activity(self,value: Optional[industry_data_activity.IndustryDataActivity] = None) -> None:
        """
        Sets the activity property value. The flow that was run by this activity.
        Args:
            value: Value to set for the activity property.
        """
        self._activity = value
    
    @property
    def blocking_error(self,) -> Optional[public_error.PublicError]:
        """
        Gets the blockingError property value. An error object to diagnose critical failures in an activity.
        Returns: Optional[public_error.PublicError]
        """
        return self._blocking_error
    
    @blocking_error.setter
    def blocking_error(self,value: Optional[public_error.PublicError] = None) -> None:
        """
        Sets the blockingError property value. An error object to diagnose critical failures in an activity.
        Args:
            value: Value to set for the blocking_error property.
        """
        self._blocking_error = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new industryDataRunActivity and sets the default values.
        """
        super().__init__()
        # The flow that was run by this activity.
        self._activity: Optional[industry_data_activity.IndustryDataActivity] = None
        # An error object to diagnose critical failures in an activity.
        self._blocking_error: Optional[public_error.PublicError] = None
        # The name of the running flow.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The status property
        self._status: Optional[industry_data_activity_status.IndustryDataActivityStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IndustryDataRunActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IndustryDataRunActivity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IndustryDataRunActivity()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the running flow.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the running flow.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "activity": lambda n : setattr(self, 'activity', n.get_object_value(industry_data_activity.IndustryDataActivity)),
            "blockingError": lambda n : setattr(self, 'blocking_error', n.get_object_value(public_error.PublicError)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(industry_data_activity_status.IndustryDataActivityStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("activity", self.activity)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[industry_data_activity_status.IndustryDataActivityStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[industry_data_activity_status.IndustryDataActivityStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[industry_data_activity_status.IndustryDataActivityStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

