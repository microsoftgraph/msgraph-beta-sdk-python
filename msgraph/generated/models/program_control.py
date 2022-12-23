from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
program = lazy_import('msgraph.generated.models.program')
program_resource = lazy_import('msgraph.generated.models.program_resource')
user_identity = lazy_import('msgraph.generated.models.user_identity')

class ProgramControl(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new programControl and sets the default values.
        """
        super().__init__()
        # The controlId of the control, in particular the identifier of an access review. Required on create.
        self._control_id: Optional[str] = None
        # The programControlType identifies the type of program control - for example, a control linking to guest access reviews. Required on create.
        self._control_type_id: Optional[str] = None
        # The creation date and time of the program control.
        self._created_date_time: Optional[datetime] = None
        # The name of the control.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The user who created the program control.
        self._owner: Optional[user_identity.UserIdentity] = None
        # The program this control is part of.
        self._program: Optional[program.Program] = None
        # The programId of the program this control is a part of. Required on create.
        self._program_id: Optional[str] = None
        # The resource, a group or an app, targeted by this program control's access review.
        self._resource: Optional[program_resource.ProgramResource] = None
        # The life cycle status of the control.
        self._status: Optional[str] = None
    
    @property
    def control_id(self,) -> Optional[str]:
        """
        Gets the controlId property value. The controlId of the control, in particular the identifier of an access review. Required on create.
        Returns: Optional[str]
        """
        return self._control_id
    
    @control_id.setter
    def control_id(self,value: Optional[str] = None) -> None:
        """
        Sets the controlId property value. The controlId of the control, in particular the identifier of an access review. Required on create.
        Args:
            value: Value to set for the controlId property.
        """
        self._control_id = value
    
    @property
    def control_type_id(self,) -> Optional[str]:
        """
        Gets the controlTypeId property value. The programControlType identifies the type of program control - for example, a control linking to guest access reviews. Required on create.
        Returns: Optional[str]
        """
        return self._control_type_id
    
    @control_type_id.setter
    def control_type_id(self,value: Optional[str] = None) -> None:
        """
        Sets the controlTypeId property value. The programControlType identifies the type of program control - for example, a control linking to guest access reviews. Required on create.
        Args:
            value: Value to set for the controlTypeId property.
        """
        self._control_type_id = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The creation date and time of the program control.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The creation date and time of the program control.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProgramControl:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProgramControl
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ProgramControl()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the control.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the control.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "control_id": lambda n : setattr(self, 'control_id', n.get_str_value()),
            "control_type_id": lambda n : setattr(self, 'control_type_id', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "owner": lambda n : setattr(self, 'owner', n.get_object_value(user_identity.UserIdentity)),
            "program": lambda n : setattr(self, 'program', n.get_object_value(program.Program)),
            "program_id": lambda n : setattr(self, 'program_id', n.get_str_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(program_resource.ProgramResource)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def owner(self,) -> Optional[user_identity.UserIdentity]:
        """
        Gets the owner property value. The user who created the program control.
        Returns: Optional[user_identity.UserIdentity]
        """
        return self._owner
    
    @owner.setter
    def owner(self,value: Optional[user_identity.UserIdentity] = None) -> None:
        """
        Sets the owner property value. The user who created the program control.
        Args:
            value: Value to set for the owner property.
        """
        self._owner = value
    
    @property
    def program(self,) -> Optional[program.Program]:
        """
        Gets the program property value. The program this control is part of.
        Returns: Optional[program.Program]
        """
        return self._program
    
    @program.setter
    def program(self,value: Optional[program.Program] = None) -> None:
        """
        Sets the program property value. The program this control is part of.
        Args:
            value: Value to set for the program property.
        """
        self._program = value
    
    @property
    def program_id(self,) -> Optional[str]:
        """
        Gets the programId property value. The programId of the program this control is a part of. Required on create.
        Returns: Optional[str]
        """
        return self._program_id
    
    @program_id.setter
    def program_id(self,value: Optional[str] = None) -> None:
        """
        Sets the programId property value. The programId of the program this control is a part of. Required on create.
        Args:
            value: Value to set for the programId property.
        """
        self._program_id = value
    
    @property
    def resource(self,) -> Optional[program_resource.ProgramResource]:
        """
        Gets the resource property value. The resource, a group or an app, targeted by this program control's access review.
        Returns: Optional[program_resource.ProgramResource]
        """
        return self._resource
    
    @resource.setter
    def resource(self,value: Optional[program_resource.ProgramResource] = None) -> None:
        """
        Sets the resource property value. The resource, a group or an app, targeted by this program control's access review.
        Args:
            value: Value to set for the resource property.
        """
        self._resource = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("controlId", self.control_id)
        writer.write_str_value("controlTypeId", self.control_type_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("owner", self.owner)
        writer.write_object_value("program", self.program)
        writer.write_str_value("programId", self.program_id)
        writer.write_object_value("resource", self.resource)
        writer.write_str_value("status", self.status)
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. The life cycle status of the control.
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. The life cycle status of the control.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

