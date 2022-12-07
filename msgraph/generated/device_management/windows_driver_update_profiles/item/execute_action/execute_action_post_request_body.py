from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

driver_approval_action = lazy_import('msgraph.generated.models.driver_approval_action')

class ExecuteActionPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the executeAction method.
    """
    @property
    def action_name(self,) -> Optional[driver_approval_action.DriverApprovalAction]:
        """
        Gets the actionName property value. An enum type to represent approval actions of single or list of drivers.
        Returns: Optional[driver_approval_action.DriverApprovalAction]
        """
        return self._action_name
    
    @action_name.setter
    def action_name(self,value: Optional[driver_approval_action.DriverApprovalAction] = None) -> None:
        """
        Sets the actionName property value. An enum type to represent approval actions of single or list of drivers.
        Args:
            value: Value to set for the actionName property.
        """
        self._action_name = value
    
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new executeActionPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # An enum type to represent approval actions of single or list of drivers.
        self._action_name: Optional[driver_approval_action.DriverApprovalAction] = None
        # The deploymentDate property
        self._deployment_date: Optional[datetime] = None
        # The driverIds property
        self._driver_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExecuteActionPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExecuteActionPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExecuteActionPostRequestBody()
    
    @property
    def deployment_date(self,) -> Optional[datetime]:
        """
        Gets the deploymentDate property value. The deploymentDate property
        Returns: Optional[datetime]
        """
        return self._deployment_date
    
    @deployment_date.setter
    def deployment_date(self,value: Optional[datetime] = None) -> None:
        """
        Sets the deploymentDate property value. The deploymentDate property
        Args:
            value: Value to set for the deploymentDate property.
        """
        self._deployment_date = value
    
    @property
    def driver_ids(self,) -> Optional[List[str]]:
        """
        Gets the driverIds property value. The driverIds property
        Returns: Optional[List[str]]
        """
        return self._driver_ids
    
    @driver_ids.setter
    def driver_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the driverIds property value. The driverIds property
        Args:
            value: Value to set for the driverIds property.
        """
        self._driver_ids = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action_name": lambda n : setattr(self, 'action_name', n.get_enum_value(driver_approval_action.DriverApprovalAction)),
            "deployment_date": lambda n : setattr(self, 'deployment_date', n.get_datetime_value()),
            "driver_ids": lambda n : setattr(self, 'driver_ids', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("actionName", self.action_name)
        writer.write_datetime_value("deploymentDate", self.deployment_date)
        writer.write_collection_of_primitive_values("driverIds", self.driver_ids)
        writer.write_additional_data_value(self.additional_data)
    

